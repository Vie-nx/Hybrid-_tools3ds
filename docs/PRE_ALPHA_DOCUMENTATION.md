# Versión Pre-Alpha: Extracción y manipulación de claves AES

## 📌 Descripción
Esta es la versión **pre-alpha** de un script diseñado para extraer y manipular claves AES desde archivos binarios (como `aeskeysdb.bin`). El objetivo principal es generar claves compatibles con emuladores como Citra.

---

## 🚀 Características principales
- **Extracción de claves**: Lee claves AES (KeyX, KeyY, KeyN, Common Keys) desde archivos binarios.
- **Compatibilidad con Citra**: Verifica si las claves extraídas son compatibles con el emulador Citra.
- **Generación de archivos de salida**: Guarda las claves extraídas en un archivo de texto (`aes_keys.txt`).
- **Manejo de errores**: Incluye validaciones para evitar errores comunes (por ejemplo, archivos no encontrados o claves faltantes).

---

## 🛠️ Uso del script

### Requisitos
- Python 3.x instalado.
- Archivos binarios de claves AES (por ejemplo, `aeskeysdb.bin`).

### Ejecución
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/aes-hybrid-keys-research.git
   cd aes-hybrid-keys-research
