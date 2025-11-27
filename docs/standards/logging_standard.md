# Logging Standard / Стандарт логирования

## 🇬🇧 English Version

### Purpose
Ensure consistent, reliable and secure logging across all microservices.

### Goals
- Human-friendly logs in development
- Structured JSON logs in production
- Support for `request_id` and `trace_id`
- No sensitive data in logs
- Compatible with ELK / Loki / Grafana / Prometheus / OpenTelemetry
- Unified logging practices across services

### Log Levels
| Level | Description |
|---|---|
| DEBUG | Debugging in development |
| INFO | Normal service events, lifecycle logs |
| WARNING | Recoverable issues, retries, timeouts |
| ERROR | Errors affecting business logic |
| CRITICAL | System failure, cannot continue |

### Required Fields
Each log entry MUST contain:
- timestamp
- level
- service_name
- message
- module and line number
- request_id (if available)
- trace_id (if available)

### Development Format (Human readable)
- Color output
- Stack traces
- Context info (file, line, function)

### Production Format (JSON structured)
Example:
```json
{
  "timestamp": "2025-01-01T12:00:00Z",
  "level": "INFO",
  "service": "course_service",
  "message": "Course created",
  "request_id": "abc123",
  "trace_id": "xyz789"
}
```

### Rules
- DO NOT log tokens, passwords, personal data
- DO NOT log sensitive configs or secrets
- Log service startup and shutdown
- Log external service failures
- Log retries and degraded modes as WARN
- Use request_id for all logs in request context

### Recommended Tools
- Loguru for application logs
- Loki + Grafana for aggregation
- OpenTelemetry for tracing
- Prometheus for metrics

---

## 🇷🇺 Русская версия

### Назначение
Обеспечить единый, безопасный и удобный формат логирования во всех микросервисах проекта.

### Цели
- Удобные логи для разработки
- JSON-логи для продакшена
- Поддержка `request_id` и `trace_id`
- Отсутствие секретов и личных данных в логах
- Совместимость с системами мониторинга и трассировки
- Единый стиль логирования

### Уровни логов
| Уровень | Значение |
|---|---|
| DEBUG | Отладка во время разработки |
| INFO | Нормальные события сервиса |
| WARNING | Восстанавливаемые ошибки (retry, timeout) |
| ERROR | Ошибка бизнес-логики или внешнего сервиса |
| CRITICAL | Критическая ошибка, сервис не может продолжать |

### Обязательные поля
Каждая запись **должна содержать**:
- время
- уровень лога
- имя сервиса
- сообщение
- файл и строку
- request_id (если есть)
- trace_id (если есть)

### Формат для разработки
- Цветные логи
- Понятные сообщения
- Отображение стека ошибок

### Формат для продакшена (JSON)
Пример:
```json
{
  "timestamp": "2025-01-01T12:00:00Z",
  "level": "INFO",
  "service": "course_service",
  "message": "Курс создан",
  "request_id": "abc123",
  "trace_id": "xyz789"
}
```

### Правила
- НЕ логировать пароли, токены, cookies, personal data (PII)
- НЕ логировать большие payload-ы
- Ошибки — всегда через ERROR или CRITICAL
- Логировать старт и остановку сервиса
- WARN — на проблемы, которые решаются retry
- request_id — обязателен для корреляции запросов

### Рекомендуемые инструменты
- Loguru (Python)
- Loki + Grafana
- OpenTelemetry/Jaeger
- Prometheus (метрики)

---

## ✅ Footer

> This document defines the standard logging policy for all services in this project.  
> Этот документ определяет стандарт логирования для всех сервисов проекта.
