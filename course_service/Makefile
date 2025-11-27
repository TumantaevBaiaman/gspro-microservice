PROTO_DIR=../shared/protos
GEN_DIR=./generated

PROTO_FILES=$(wildcard $(PROTO_DIR)/course/*.proto)

$(GEN_DIR)/course/__init__.py:
	mkdir -p $(GEN_DIR)/course
	touch $(GEN_DIR)/__init__.py
	touch $(GEN_DIR)/course/__init__.py

$(GEN_DIR)/course_pb2.py: $(wildcard $(PROTO_DIR)/course/*.proto) $(GEN_DIR)/course/__init__.py
	python -m grpc_tools.protoc -I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(wildcard $(PROTO_DIR)/course/*.proto)
	if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from course import course_pb2|from generated.course import course_pb2|' $(GEN_DIR)/course/course_pb2_grpc.py; \
	else \
		sed -i 's|from course import course_pb2|from generated.course import course_pb2|' $(GEN_DIR)/course/course_pb2_grpc.py; \
	fi

proto: $(GEN_DIR)/course_pb2.py
	@echo "✅ Proto files are up to date"