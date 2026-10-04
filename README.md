# mini-distributed-Google-Drive

## motive -> 
to design a mini distributed system trying to mimick google drive

# architecture (will evolve with time):

                    ┌──────────────────────┐
                    │      React UI        │
                    │  Google Drive-like   │
                    └──────────┬───────────┘
                               │
                         REST / WebSocket
                               │
                    ┌──────────▼───────────┐
                    │      API Server      │
                    │       FastAPI        │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
          ┌──────▼──────┐             ┌──────▼──────┐
          │  PostgreSQL │             │   Auth/User │
          │   Metadata  │             │   Service   │
          └─────────────┘             └─────────────┘
                 │
                 ▼
          ┌───────────────┐
          │ Storage Layer │
          └───────┬───────┘
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
   ┌────────┐ ┌────────┐ ┌────────┐
   │ Node 1 │ │ Node 2 │ │ Node 3 │
   │ Disk   │ │ Disk   │ │ Disk   │
   └────────┘ └────────┘ └────────┘
       │          │          │
       └──────┬───┴──────┬───┘
              │          │
        shards / replicas



# architecture 
<img width="617" height="415" alt="Screenshot 2026-10-04 at 6 21 50 PM" src="https://github.com/user-attachments/assets/ee238f22-b4c8-46d5-a251-5fdd85bd25cc" />


        
