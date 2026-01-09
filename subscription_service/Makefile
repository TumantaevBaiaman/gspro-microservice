PROTO_DIR=../shared/protos/subscription
GEN_DIR=./generated/subscription

PROTO_FILES=$(wildcard $(PROTO_DIR)/*.proto)

$(GEN_DIR):
	mkdir -p $(GEN_DIR)
	touch $(GEN_DIR)/__init__.py

proto: $(GEN_DIR)
	@for file in $(PROTO_FILES); do \
		echo "📦 Generating for $$file"; \
		python -m grpc_tools.protoc -I=$(PROTO_DIR) \
			--python_out=$(GEN_DIR) \
			--grpc_python_out=$(GEN_DIR) \
			$$file; \
	done

	@if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|import \(.*_pb2\)|from generated.subscription import \1|' $(GEN_DIR)/*_grpc.py; \
	else \
		sed -i 's|import \(.*_pb2\)|from generated.subscription import \1|' $(GEN_DIR)/*_grpc.py; \
	fi

	@echo "✅ Generation complete!"
