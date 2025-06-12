# DBATIVE

Welcome to **DBATIVE**, a FastAPI-based project demonstrating CRUD routes, a self-referential `Category`, and a layered architecture with Services and Repositories. Below you will find setup instructions, architecture notes, and Mermaid diagrams.

---

## How to Run

1. **Install dependencies** (assuming you have Python 3.10+):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt



   ```

2. Start the API
   uvicorn main:app --reload

3. Explore the API Docs via Swagger UI at:
   http://127.0.0.1:8000/docs

4.Layered Architecture
We have four main layers:

Presentation Layer (Routes): Handles HTTP requests/responses and routes.
Application Layer (Services): Contains business logic and transformations.
Domain Layer (Entities/Models): Defines the core domain objects.
Persistence Layer (Repositories, Database): Handles data access and storage.

erDiagram
USER ||--|{ TRANSACTION : "makes"
USER {
int id PK
string full_name
string email
string hashed_password
}
TRANSACTION {
int id PK
decimal amount
int buyer_id
int seller_id
}
TRANSACTION }|--|| USER : "belongs to"

    CATEGORY ||--|{ CATEGORY : "self reference with parent/child"
    CATEGORY {
        int id PK
        string name
        string description
        string slug
        int parent_id
    }

    USEDPRODUCT {
        int id PK
        string name
        float price
        int age_in_months
    }

flowchart LR
A[Presentation Layer (Routes)] --> B[Application Layer (Services)]
B --> C[Domain Layer (Entities/Models)]
B --> D[Persistence Layer (Repositories, DB)]

sequenceDiagram
participant Client
participant API
participant ExternalService

    Client->>API: POST /transactions
    API->>ExternalService: Verify Payment
    ExternalService->>API: Payment status
    API->>Client: HTTP 201 Created
