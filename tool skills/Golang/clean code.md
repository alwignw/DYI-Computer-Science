Struktur folder ini dibuat supaya project Software Engineering di Go Programming Language:

* mudah di-maintain
* scalable
* tidak spaghetti code
* gampang testing
* gampang onboarding team
* mudah dipisah jadi microservice nanti

---

# Gambaran Besar Arsitektur

Alurnya:

```txt id="uhydx3"
Request HTTP
    ↓
Handler / Controller
    ↓
Service / Usecase
    ↓
Repository
    ↓
Database / Redis
```

Jadi tiap layer punya tanggung jawab sendiri.

---

# Struktur Folder

```txt id="jlwmic"
golang-clean-architecture/
│
├── cmd/
├── config/
├── internal/
├── pkg/
├── migrations/
├── docs/
├── .env
└── docker-compose.yml
```

---

# 1. `cmd/`

```txt id="95ndj8"
cmd/
 └── api/
      └── main.go
```

## Fungsi

Tempat entry point aplikasi.

Biasanya:

```txt id="kmjlwm"
cmd/api
cmd/worker
cmd/cron
cmd/grpc
```

---

## Kenapa Dipisah?

Karena satu project Go bisa punya banyak executable.

Contoh:

```txt id="7rq4or"
API Server
Queue Worker
Cron Job
CLI Tool
```

Semua bisa share logic yang sama.

---

## Isi `main.go`

Tugasnya hanya:

* load config
* init db
* init redis
* init routes
* dependency injection
* start server

JANGAN isi business logic.

---

# 2. `config/`

```txt id="jlwmm4"
config/
 └── config.go
```

## Fungsi

Load:

* env
* config app
* secret
* timeout
* app setting

---

## Kenapa Dipisah?

Supaya:

```txt id="jlwmte"
os.Getenv(...)
```

tidak tersebar dimana-mana.

---

## Best Practice

Biasanya ada:

```txt id="jlwm7n"
config/
 ├── app.go
 ├── db.go
 ├── redis.go
 └── jwt.go
```

---

# 3. `internal/`

INI PALING PENTING.

```txt id="jlwmj0"
internal/
 ├── domain/
 ├── repository/
 ├── service/
 ├── handler/
 └── routes/
```

---

# Kenapa Namanya `internal`?

Fitur bawaan Go.

Package dalam `internal/`:

```txt id="jlwmh7"
TIDAK BISA di-import project lain
```

Jadi aman untuk private business logic.

---

# 4. `internal/domain/`

```txt id="jlwm2l"
domain/
 └── user.go
```

## Fungsi

Representasi business entity.

Contoh:

```go id="jlwmqr"
type User struct {
	ID    uuid.UUID
	Name  string
	Email string
}
```

---

## Domain Itu Apa?

Bukan database.

Tapi representasi bisnis.

Contoh:

```txt id="g3cewx"
User
Order
Invoice
Payment
Product
```

---

# 5. `internal/repository/`

```txt id="jlwmop"
repository/
 └── user_repository.go
```

## Fungsi

Layer akses data.

Semua query DB disini.

---

## Tanggung Jawab

* SELECT
* INSERT
* UPDATE
* DELETE

---

## Kenapa Dipisah?

Supaya service tidak tahu SQL.

Jadi:

```txt id="bjlwmk"
service fokus bisnis
repository fokus data
```

---

## Contoh

```go id="jlwmwl"
func (r *UserRepository) FindAll()
```

---

# 6. `internal/service/`

```txt id="jlwmk9"
service/
 └── user_service.go
```

## Fungsi

Business logic utama.

---

## Isi Service

Contoh:

```txt id="jlwm0y"
validasi bisnis
hitung diskon
workflow
integrasi external API
transaction
cache logic
```

---

## Contoh

```go id="4gjlwm"
func (s *UserService) CreateUser()
```

---

# Kenapa Penting?

Karena:

```txt id="jlwm3y"
handler jangan pintar
repository jangan pintar
```

Business logic harus di service.

---

# 7. `internal/handler/`

```txt id="jlwmnd"
handler/
 └── user_handler.go
```

## Fungsi

Terima request HTTP.

---

## Tugas Handler

* baca request
* parse JSON
* validasi request basic
* panggil service
* return response

---

## Handler JANGAN:

* query database
* business logic besar
* hitung-hitung bisnis

---

## Contoh

```go id="jlwmta"
func (h *UserHandler) GetUsers(c *gin.Context)
```

---

# 8. `internal/routes/`

```txt id="jlwmxk"
routes/
 └── routes.go
```

## Fungsi

Semua endpoint routing.

---

## Contoh

```go id="0kjlwm"
api.GET("/users", userHandler.GetUsers)
```

---

## Kenapa Dipisah?

Supaya `main.go` bersih.

---

# 9. `pkg/`

```txt id="jlwmjc"
pkg/
 ├── database/
 └── redis/
```

## Fungsi

Reusable/shared package.

---

## Bedanya Dengan `internal`

| internal                  | pkg      |
| ------------------------- | -------- |
| private app               | reusable |
| business logic            | utility  |
| tidak boleh diimport luar | boleh    |

---

## Isi pkg Biasanya

```txt id="jlwmk4"
logger
jwt
database
redis
mailer
validator
response
pagination
```

---

# 10. `pkg/database/`

```txt id="jlwm3q"
database/
 └── postgres.go
```

## Fungsi

Connection database.

---

# 11. `pkg/redis/`

```txt id="8jlwm8"
redis/
 └── redis.go
```

## Fungsi

Connection Redis.

---

# 12. `migrations/`

```txt id="jlwmq1"
migrations/
```

## Fungsi

SQL versioning.

---

## Isi

```sql id="jlwm5z"
001_create_users.sql
002_create_products.sql
003_add_index.sql
```

---

## Kenapa Penting?

Supaya schema database:

```txt id="0jlwmc"
consistent antar developer
```

---

# 13. `docs/`

```txt id="jlwm8f"
docs/
```

## Fungsi

Swagger generated files.

Generated otomatis oleh:

```bash id="jlwm3m"
swag init
```

---

# 14. `.env`

## Fungsi

Environment variable.

---

## Contoh

```env id="jlwmw7"
DB_HOST=
DB_USER=
JWT_SECRET=
```

---

# 15. `docker-compose.yml`

## Fungsi

Menjalankan dependency lokal.

Contoh:

* PostgreSQL
* Redis
* Kafka
* Minio

---

# Dependency Flow

Flow dependency yang benar:

```txt id="jlwm7u"
handler
   ↓
service
   ↓
repository
   ↓
database
```

BUKAN:

```txt id="2jlwmx"
repository -> handler
service -> handler
```

---

# Kenapa Ini Disebut Clean Architecture?

Karena:

* dependency terarah
* business logic terisolasi
* mudah test
* scalable
* framework tidak mengontrol core logic

---

# Ketika Project Membesar

Biasanya berkembang jadi:

```txt id="jlwmgq"
internal/
 ├── user/
 │    ├── handler/
 │    ├── service/
 │    ├── repository/
 │    ├── dto/
 │    └── domain/
 │
 ├── auth/
 ├── payment/
 ├── product/
```

Ini disebut:

```txt id="xjlwm5"
feature based architecture
```

dan sangat umum di backend enterprise Go modern.

---

# Yang Biasanya Ditambahkan Lagi

Production-grade biasanya tambah:

```txt id="5jlwmv"
middleware/
dto/
validator/
response/
helper/
exceptions/
logger/
queue/
scheduler/
storage/
integration/
```

---

# Struktur Ini Cocok Untuk

* REST API
* CRM
* ERP
* Microservice
* SaaS
* AI Backend
* Authentication Server
* Payment Gateway
* Queue Worker

Karena separation of concern-nya jelas.
