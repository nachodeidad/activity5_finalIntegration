RutasTiyei - Mapa Interactivo Accesible - Tijuana, BC
Una plataforma interactiva de un mapa que combina geolocalización, cálculo de rutas y principios de los diseños para la experiencia de usuario.

Como ejecutar el proyecto:
Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno

Instalación y ejecución:

- git clone https://github.com/nachodeidad/activity5_finalIntegration
- cd activity5_finalIntegration

- pip install flask
- python app.py

Abrir en el navegador:
- http://localhost:5000

La aplicación se abrirá automáticamente y te mandará a una landing page, al presionar el botón "ver demo" te mandará al mapa interactivo el cual solicitará permisos de ubicación, se debe dar "aceptar" para usar
completamente la aplicación.

Stack Tecnológico:
**Backend**
Flask 3.0+ - Framework web minimalista de Python
- Routing dinámico
- Renderizado de templates Jinja2
- Servidor de desarrollo integrado



**Frontend**
- HTML5 - Estructura semántica y accesible
- CSS3 - Estilos modernos con animaciones fluidas
- JavaScript (ES6+) - Lógica de interacción y geolocalización
- Tailwind CSS - Framework de utilidades para diseño responsive
- Leaflet.js 1.9.4 - Biblioteca de mapas interactivos

- OpenStreetMap como proveedor de tiles
- Soporte para marcadores personalizados
- Sistema de popups y tooltips

**APIs y Servicios**
-Geolocation API - Detección automática de ubicación del usuario
- OSRM (Open Source Routing Machine) - Cálculo de rutas optimizadas
- OpenStreetMap - Mapas de código abierto

**Diseño**
- Diseño Responsive - Adaptable a móvil, tablet y escritorio
- Accesibilidad WCAG 2.1 AA - Atributos ARIA, navegación por teclado
- Alto Contraste - Colores optimizados para visibilidad

**Justificación de Diseño**
Principios de UX Implementados
1. Accesibilidad Universal
Basándonos en las mejores prácticas de diseño inclusivo, se implementó:

- Alternativas Textuales: Vista de lista sincronizada que permite a usuarios con discapacidad visual acceder a toda la información sin depender exclusivamente del mapa visual
- Navegación por Teclado: Todos los elementos interactivos son accesibles mediante Tab, Enter y Espacio
- Atributos ARIA: Labels descriptivos en todos los controles (aria-label, role, aria-live)

Contraste Optimizado:
- Marcadores con bordes gruesos (4-5px) y sombras para destacar sobre cualquier fondo de mapa
- Rojo brillante (#dc2626) para puntos guardados vs. amarillo (#fbbf24) para temporales
- Ratio de contraste superior a 4.5:1 en todos los textos



2. Diseño Responsive y Mobile-First

- Sistema de Pestañas en Móvil: Cambio intuitivo entre vistas Mapa/Lista
- Columnas Duales en Desktop: Aprovechamiento del espacio en pantallas grandes
- Botones Táctiles: Tamaño mínimo de 44x44px siguiendo estándares de accesibilidad
- Adaptación por Orientación: Layout optimizado para landscape en dispositivos móviles

3. Sincronización Bidireccional
Inspirado en principios de consistencia y retroalimentación inmediata:

Mapa → Lista: Cada marcador agregado se refleja instantáneamente en la lista textual
Lista → Mapa: Clic en un ítem dispara animación flyTo hacia el marcador correspondiente
Indicadores Visuales: Resaltado temporal del ítem activo en la lista

4. Feedback Continuo al Usuario

Notificaciones Toast: Sistema no intrusivo con iconografía clara (éxito, error, info)
Estados de Carga: Spinners durante operaciones asíncronas (geolocalización, cálculo de rutas)
Mensajes Contextuales: Instrucciones claras sobre límites (máximo 2 puntos) y acciones disponibles

5. Geolocalización Automática

Detección al Cargar: El mapa se centra automáticamente en la ubicación del usuario
Marcador Pulsante: Animación CSS que indica la posición actual con círculo expansivo

6. Cálculo Inteligente de Rutas

Rutas por Calles: Integración con OSRM para rutas reales conducibles
Fallback a Línea Directa: Si falla el routing, muestra distancia en línea recta
Información Contextual: Distancia en km y tiempo estimado en minutos
Visualización Diferenciada:

- Azul sólido para rutas calculadas
- Rojo punteado para líneas directas

--------------------------------------------------------------------------------------------------------------
Créditos a la IA
Este código fue co-creado con Claude
Prompts Principales Utilizados:
Crea una Landing Page HTML para una app de mapas llamada [NOMBRE]. Debe tener un 'Hero' con una imagen de fondo de un mapa estilizado o topográfico, un título grande, y un botón CTA prominente que diga 'Explorar Mapa'. Usa Tailwind CSS. El diseño debe inspirar aventura/seguridad.

Genera un archivo HTML que incluya la librería Leaflet.js (vía CDN) y Tailwind CSS. Crea un contenedor div 'map' que ocupe el 100% del ancho y 500px de alto (o 'h-screen'). Inicializa el mapa centrado en [TU CIUDAD] con un tilelayer de OpenStreetMap. Asegúrate de que los botones de zoom estén en una posición fácil de alcanzar.

Escribe un script en JS para Leaflet. Cuando el usuario haga clic en el mapa: 1. Ponga un marcador temporal inmediatamente. 2. Abra un popup que pregunte '¿Guardar este punto?'. 3. Al confirmar, envíe las coordenadas (lat, long) a un endpoint Flask /guardar_punto usando fetch. Muestra un 'toast' o notificación de 'Guardando...' mientras se procesa.

Modifica la interfaz para tener dos columnas (o pestañas en móvil): 'Mapa' y 'Lista de Lugares'. Cuando se agregue un marcador en el mapa, debe aparecer también como un texto descriptivo en la sección de Lista (ej. 'Punto en Lat: X, Long: Y'). Asegúrate de que los botones del mapa tengan atributos 'aria-label' como 'Acercar mapa' o 'Alejar mapa'.

