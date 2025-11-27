PROTO_DIR=../shared/protos
GEN_DIR=./generated

USER_PROTO_FILES=$(wildcard $(PROTO_DIR)/user/*.proto)
COURSE_PROTO_FILES=$(wildcard $(PROTO_DIR)/course/*.proto)

# ===== USER =====

$(GEN_DIR)/user/__init__.py:
	mkdir -p $(GEN_DIR)/user
	touch $(GEN_DIR)/__init__.py
	touch $(GEN_DIR)/user/__init__.py

$(GEN_DIR)/user_pb2.py: $(USER_PROTO_FILES) $(GEN_DIR)/user/__init__.py
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(USER_PROTO_FILES)

	if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from user import user_pb2|from generated.user import user_pb2|' $(GEN_DIR)/user/user_pb2_grpc.py; \
	else \
		sed -i 's|from user import user_pb2|from generated.user import user_pb2|' $(GEN_DIR)/user/user_pb2_grpc.py; \
	fi

# ===== COURSE =====

$(GEN_DIR)/course/__init__.py:
	mkdir -p $(GEN_DIR)/course
	touch $(GEN_DIR)/__init__.py
	touch $(GEN_DIR)/course/__init__.py

$(GEN_DIR)/course_pb2.py: $(COURSE_PROTO_FILES) $(GEN_DIR)/course/__init__.py
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(COURSE_PROTO_FILES)

	if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from course import course_pb2|from generated.course import course_pb2|' $(GEN_DIR)/course/course_pb2_grpc.py; \
	else \
		sed -i 's|from course import course_pb2|from generated.course import course_pb2|' $(GEN_DIR)/course/course_pb2_grpc.py; \
	fi

# ===== GENERAL TARGET =====

proto: $(GEN_DIR)/user_pb2.py $(GEN_DIR)/course_pb2.py
	@echo "✅ Proto files are up to date"
