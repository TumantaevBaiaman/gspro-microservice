PROTO_DIR=../shared/protos
GEN_DIR=generated

USER_PROTO_FILES=$(wildcard $(PROTO_DIR)/user/*.proto)
COURSE_PROTO_FILES=$(wildcard $(PROTO_DIR)/course/*.proto)
REVIEWS_PROTO_FILES=$(wildcard $(PROTO_DIR)/reviews/*.proto)
FAVORITES_PROTO_FILES=$(wildcard $(PROTO_DIR)/favorites/*.proto)
CHAT_PROTO_FILES=$(wildcard $(PROTO_DIR)/chat/*.proto)
MEDIA_PROTO_FILES=$(wildcard $(PROTO_DIR)/media/*.proto)
SUBSCRIPTION_PROTO_FILES=$(wildcard $(PROTO_DIR)/subscription/*.proto)
PROGRESS_PROTO_FILES=$(wildcard $(PROTO_DIR)/progress/*.proto)


init:
	mkdir -p $(GEN_DIR)/user
	mkdir -p $(GEN_DIR)/course
	mkdir -p $(GEN_DIR)/reviews
	mkdir -p $(GEN_DIR)/favorites
	mkdir -p $(GEN_DIR)/chat
	mkdir -p $(GEN_DIR)/media
	mkdir -p $(GEN_DIR)/subscription
	mkdir -p $(GEN_DIR)/progress
	touch $(GEN_DIR)/__init__.py
	touch $(GEN_DIR)/user/__init__.py
	touch $(GEN_DIR)/course/__init__.py
	touch $(GEN_DIR)/reviews/__init__.py
	touch $(GEN_DIR)/favorites/__init__.py
	touch $(GEN_DIR)/chat/__init__.py
	touch $(GEN_DIR)/media/__init__.py
	touch $(GEN_DIR)/subscription/__init__.py
	touch $(GEN_DIR)/progress/__init__.py


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


favorites_proto: init
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(FAVORITES_PROTO_FILES)

	@if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from favorites import \(.*_pb2\)|from generated.favorites import \1|' $(GEN_DIR)/favorites/*_grpc.py; \
	else \
		sed -i 's|from favorites import \(.*_pb2\)|from generated.favorites import \1|' $(GEN_DIR)/favorites/*_grpc.py; \
	fi


chat_proto: init
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(CHAT_PROTO_FILES)

	@if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from chat import \(.*_pb2\)|from generated.chat import \1|' $(GEN_DIR)/chat/*_grpc.py; \
	else \
		sed -i 's|from chat import \(.*_pb2\)|from generated.chat import \1|' $(GEN_DIR)/chat/*_grpc.py; \
	fi


media_proto: init
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(MEDIA_PROTO_FILES)

	@if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from media import \(.*_pb2\)|from generated.media import \1|' $(GEN_DIR)/media/*_grpc.py; \
	else \
		sed -i 's|from media import \(.*_pb2\)|from generated.media import \1|' $(GEN_DIR)/media/*_grpc.py; \
	fi


subscription_proto: init
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(SUBSCRIPTION_PROTO_FILES)

	@if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from subscription import \(.*_pb2\)|from generated.subscription import \1|' $(GEN_DIR)/subscription/*_grpc.py; \
	else \
		sed -i 's|from subscription import \(.*_pb2\)|from generated.subscription import \1|' $(GEN_DIR)/subscription/*_grpc.py; \
	fi


progress_proto: init
	python -m grpc_tools.protoc \
		-I=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(PROGRESS_PROTO_FILES)

	@if [ "$(shell uname)" = "Darwin" ]; then \
		sed -i '' 's|from progress import \(.*_pb2\)|from generated.progress import \1|' $(GEN_DIR)/progress/*_grpc.py; \
	else \
		sed -i 's|from progress import \(.*_pb2\)|from generated.progress import \1|' $(GEN_DIR)/progress/*_grpc.py; \
	fi



proto: course_proto user_proto reviews_proto favorites_proto chat_proto media_proto subscription_proto progress_proto
	@echo "Proto files generated successfully in gateway!"
