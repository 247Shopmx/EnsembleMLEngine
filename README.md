📘 README.md — SPORTS QUANT FUND (FULL PRODUCTION SYSTEM)

# 🏦 SPORTS QUANT FUND — FULL PRODUCTION TRADING SYSTEM

Sistema de trading cuantitativo deportivo en tiempo real (tipo hedge fund) con:
- Machine Learning (XGBoost / LightGBM / Neural Networks)
- Modelos probabilísticos (Poisson)
- Detección de valor (EV / Arbitrage)
- Integración con mercados de apuestas (Betfair / Pinnacle)
- Gestión de riesgo tipo hedge fund (Kelly + drawdown control)
- Arquitectura de microservicios en producción

---

# 🧠 ARQUITECTURA GENERAL

DATA INGESTION → STREAM PROCESSOR → MODEL SERVICE → PRICING ENGINE  
→ EDGE DETECTOR → RISK ENGINE → EXECUTION ENGINE → PORTFOLIO TRACKER

---

# ⚙️ COMPONENTES DEL SISTEMA

## 1. DATA INGESTION LAYER
Fuentes de datos:
- Betfair Streaming API (odds en tiempo real)
- Pinnacle API (cuotas globales)
- Live match event feeds (goles, tarjetas, xG)

Función:
Recolectar datos en tiempo real con baja latencia.

---

## 2. MODEL SERVICE (ML CORE)
Modelos incluidos:
- XGBoost classifier
- LightGBM model
- Neural network ensemble

Características:
- Predicción W/D/L
- Probabilidades calibradas
- Ensemble averaging

Calibración:
- Platt Scaling
- Isotonic Regression

---

## 3. PRICING ENGINE (PROBABILISTIC MODEL)

Modelos utilizados:
- Poisson distribution (goles esperados)
- Bayesian probability fusion

Output:
- Probabilidad home/draw/away
- Expected goals (xG estimado)

---

## 4. EDGE DETECTION ENGINE

Detecta oportunidades de valor:

- Expected Value (EV)
- Arbitrage detection
- Market inefficiencies

Fórmula base:

EV = (probabilidad × cuota) - 1

---

## 5. RISK ENGINE (GESTIÓN DE CAPITAL)

Incluye:

- Kelly Criterion
- Max exposure per trade
- Daily loss limits
- Drawdown control

Fórmula Kelly:

f* = (b·p - q) / b

---

## 6. EXECUTION ENGINE (TRADING REAL)

Función:
- Enviar órdenes a Betfair / Pinnacle
- Ejecutar apuestas en vivo
- Confirmar fills

Incluye:
- Order tracking
- Retry logic
- Execution logs

---

## 7. PORTFOLIO TRACKER

Métricas:
- PnL (Profit & Loss)
- Sharpe Ratio
- Max Drawdown
- ROI por liga

---

# 🚀 INSTALACIÓN

```bash
git clone <repo-url>
cd quant-fund
pip install -r requirements.txt


---

🐳 EJECUCIÓN CON DOCKER

docker-compose up --build


---

⚙️ EJECUCIÓN MANUAL

Model Service

cd services/model-service
uvicorn app:app --reload --port 8000

Live Trading Bot

python services/execution/live_bot.py


---

📡 API DEL MODELO

POST /predict

Request:

{
  "features": [2.1, 1.3, 0.8, 3.4]
}

Response:

{
  "home": 0.52,
  "draw": 0.23,
  "away": 0.25
}


---

💰 MOTOR DE DECISIÓN

El sistema ejecuta apuestas solo si:

EV > 0

Kelly > 0

Liquidez disponible

Riesgo dentro de límites



---

⚖️ FÓRMULAS CLAVE

Expected Value

EV = (probabilidad × cuota) - 1

Kelly Criterion

f* = (b·p - q) / b


---

📉 GESTIÓN DE RIESGO

Reglas:

Máximo 3% bankroll por apuesta

Stop-loss diario

Control de exposición por mercado

Reducción automática en drawdown



---

📊 MÉTRICAS DEL SISTEMA

Sharpe Ratio

Max Drawdown

ROI por liga

Edge promedio por apuesta

Accuracy del modelo



---

🧱 INFRAESTRUCTURA (PRODUCCIÓN)

Servicios:

model-service (FastAPI)

pricing-service

risk-engine

execution-engine

portfolio-service

redis (cache)

kafka (streaming opcional)



---

🐳 DOCKER STACK

version: "3.9"

services:
  model:
    build: ./services/model-service
    ports:
      - "8000:8000"

  risk:
    build: ./services/risk

  execution:
    build: ./services/execution

  portfolio:
    build: ./services/portfolio

  redis:
    image: redis:latest

  kafka:
    image: bitnami/kafka:latest
