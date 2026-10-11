# Ruta: web, HTTP y APIs

## Propósito

Entender cómo se intercambian datos entre programas y servicios. La ruta comienza con HTTP y JSON antes de crear una aplicación web propia.

## Secuencia

1. Comprender cliente, servidor, URL, petición y respuesta.
2. Leer y producir JSON.
3. Consultar una API pública, respetando sus límites y condiciones.
4. Gestionar errores de conexión, respuestas inesperadas y tiempos de espera.
5. Crear una aplicación web pequeña con Flask.
6. Explorar FastAPI cuando se necesite construir una API con validación y documentación automática.

## Herramientas

- Biblioteca estándar: `json` y `urllib` para comprender los conceptos básicos.
- `requests`: opción cómoda para solicitudes HTTP.
- `Flask`: primera aplicación web pequeña.
- `FastAPI`: ruta posterior para construir APIs.

No todas las rutas necesitan todas las herramientas. Para los primeros ejercicios no se deben requerir claves secretas ni servicios de pago.

## Proyectos graduados

- Básico: convertir un diccionario Python en JSON y recuperarlo.
- Inicial aplicado: consultar una API pública y mostrar algunos campos.
- Intermedio: presentar los datos en una página sencilla.
- Intermedio+: crear una API que reciba y valide información.
- Integrador: aplicación pequeña que consulte un servicio y explique cómo maneja errores.

## Buenas prácticas

- Comprueba los términos de uso y límites del servicio consultado.
- Define tiempos de espera y maneja fallos de red.
- No guardes claves secretas en el código ni en GitHub.
- Valida la información recibida; no asumas que siempre tendrá la forma esperada.
- No envíes datos personales a servicios externos sin una justificación y autorización apropiadas.

## Referencias

- [urllib — documentación de Python](https://docs.python.org/es/3/library/urllib.html)
- [JSON en Python](https://docs.python.org/es/3/library/json.html)
- [Requests](https://requests.readthedocs.io/)
- [Flask](https://flask.palletsprojects.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
