# Plataforma DePIN con IA para Optimización de Cadenas de Suministro

Una plataforma innovadora que integra dispositivos IoT (infraestructura física descentralizada - DePIN) con blockchain (Starknet) e Inteligencia Artificial para ofrecer trazabilidad, verificación y optimización en tiempo real de cadenas de suministro.

## Descripción

Este proyecto busca resolver los problemas de opacidad, ineficiencia y falta de confianza en las cadenas de suministro globales. Utilizando la inmutabilidad de la blockchain para registrar datos de sensores IoT y la potencia de la IA para analizar patrones, predecir anomalías y sugerir mejoras operativas. La privacidad y escalabilidad se aseguran mediante el uso de Starknet (Cairo/Rust).

## Arquitectura del Proyecto

El proyecto está dividido en cuatro componentes principales:

1.  **Contratos Inteligentes (Starknet/Cairo):** Gestionan la lógica de negocio descentralizada, el registro inmutable de eventos y la verificación de autenticidad.
2.  **Backend (Rust/TypeScript):** Actúa como puente entre los dispositivos IoT, la blockchain y la aplicación móvil. Expone APIs REST/GraphQL.
3.  **Módulo de IA (Python):** Procesa los datos recopilados para realizar análisis predictivo, detección de anomalías y optimización de rutas.
4.  **Aplicación Móvil (Flutter):** Proporciona una interfaz intuitiva para que los usuarios y empresas monitoreen sus cadenas de suministro en tiempo real.

Para más detalles, consulta el documento de [Arquitectura Técnica](docs/arquitectura_tecnica.md).

## Estructura del Repositorio

```text
depin-supply-chain/
├── ai_module/              # Módulo de Inteligencia Artificial (Python)
├── backend/                # Backend API (Rust/TypeScript)
├── docs/                   # Documentación técnica y de arquitectura
├── mobile_app/             # Aplicación móvil (Flutter)
├── starknet_contracts/     # Contratos inteligentes (Cairo)
├── .github/                # Templates de GitHub (Issues, PRs)
├── README.md               # Este archivo
└── ROADMAP.md              # Hoja de ruta del proyecto
```

## Configuración y Setup (Scaffold)

### Requisitos Previos

*   [Scarb](https://docs.swmansion.com/scarb/) (para compilar contratos en Cairo)
*   [Rust](https://www.rust-lang.org/) y Cargo (para el backend en Rust)
*   [Node.js](https://nodejs.org/) y npm/yarn (para el backend en TypeScript)
*   [Flutter SDK](https://flutter.dev/) (para la aplicación móvil)
*   [Python 3.8+](https://www.python.org/) (para el módulo de IA)

### 1. Contratos Inteligentes (Starknet)

```bash
cd starknet_contracts
scarb build
```

### 2. Backend (Rust o TypeScript)

**Opción Rust:**
```bash
cd backend
cargo build
cargo run
```

**Opción TypeScript:**
```bash
cd backend
npm install
npm run dev
```

### 3. Módulo de IA (Python)

```bash
cd ai_module
pip install -r requirements.txt
python app.py
```

### 4. Aplicación Móvil (Flutter)

```bash
cd mobile_app
flutter pub get
flutter run
```

## Roadmap

Consulta el archivo [ROADMAP.md](ROADMAP.md) para conocer las fases de desarrollo y los hitos del proyecto.

## Contribución

Por favor, revisa nuestros templates de [Issues](.github/ISSUE_TEMPLATE.md) y [Pull Requests](.github/PULL_REQUEST_TEMPLATE.md) antes de contribuir.

## Licencia

Este proyecto está bajo la Licencia MIT.
