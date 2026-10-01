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


        