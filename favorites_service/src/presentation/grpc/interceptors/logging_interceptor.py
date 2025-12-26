import time
import grpc
from grpc import aio

from src.core.logging.logger import logger


class LoggingInterceptor(aio.ServerInterceptor):

    async def intercept_service(self, continuation, handler_call_details):
        handler = await continuation(handler_call_details)
        if handler is None:
            return None

        method = handler_call_details.method

        if handler.unary_unary:

            async def unary_unary_interceptor(request, context):
                start = time.monotonic()

                logger.bind(
                    grpc_method=method
                ).debug(
                    "➡️ gRPC request | payload={payload}",
                    payload=request.__class__.__name__
                )

                try:
                    response = await handler.unary_unary(request, context)

                    elapsed = (time.monotonic() - start) * 1000

                    logger.bind(
                        grpc_method=method,
                        latency_ms=round(elapsed, 2),
                    ).info(
                        "✅ gRPC response"
                    )

                    return response

                except grpc.RpcError as e:
                    elapsed = (time.monotonic() - start) * 1000

                    logger.bind(
                        grpc_method=method,
                        latency_ms=round(elapsed, 2),
                        grpc_code=e.code().name,
                    ).error(
                        "❌ gRPC error | details={details}",
                        details=e.details()
                    )
                    raise

            return grpc.unary_unary_rpc_method_handler(
                unary_unary_interceptor,
                request_deserializer=handler.request_deserializer,
                response_serializer=handler.response_serializer,
            )

        return handler
