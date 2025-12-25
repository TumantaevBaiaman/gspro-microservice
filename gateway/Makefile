PROTO_DIR=../shared/protos
GEN_DIR=generated

USER_PROTO_FILES=$(wildcard $(PROTO_DIR)/user/*.proto)
COURSE_PROTO_FILES=$(wildcard $(PROTO_DIR)/course/*.proto)
REVIEWS_PROTO_FILES=$(wildcard $(PROTO_DIR)/reviews/*.proto)


init:
	mkdir -p $(GEN_DIR)/user
	mkdir -p $(GEN_DIR)/course
	touch $(GEN_DIR)/__init__.py
	touch $(GEN_DIR)/user/__init__.py
	touch $(GEN_DIR)/course/__init__.py
	touch $(GEN_DIR)/reviews/__init__.py


user_proto: init
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(USER_PROTO_FILES)

	@if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from user import \(.*_pb2\)|from generated.user import \1|' $(GEN_DIR)/user/*_grpc.py; \
	else \
		sed -i 's|from user import \(.*_pb2\)|from generated.user import \1|' $(GEN_DIR)/user/*_grpc.py; \
	fi


course_proto: init
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(COURSE_PROTO_FILES)

	@if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from course import \(.*_pb2\)|from generated.course import \1|' $(GEN_DIR)/course/*_grpc.py; \
	else \
		sed -i 's|from course import \(.*_pb2\)|from generated.course import \1|' $(GEN_DIR)/course/*_grpc.py; \
	fi


reviews_proto: init
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(REVIEWS_PROTO_FILES)

	@if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from reviews import \(.*_pb2\)|from generated.reviews import \1|' $(GEN_DIR)/reviews/*_grpc.py; \
	else \
		sed -i 's|from reviews import \(.*_pb2\)|from generated.reviews import \1|' $(GEN_DIR)/reviews/*_grpc.py; \
	fi



proto: course_proto user_proto reviews_proto
	@echo "🚀 Proto files generated successfully in gateway!"
