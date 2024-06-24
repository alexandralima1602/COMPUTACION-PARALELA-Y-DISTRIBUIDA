## Proyecto 3: Orquestación de microservicios con Docker y Kubernetes – Alejandra Lima 
Objetivo del Proyecto: 

Desarrollar y orquestar una arquitectura de microservicios utilizando Flask, Docker y Kubernetes 
para implementar una aplicación web escalable y modular. 
Sprint 1: Diseño y desarrollo de una arquitectura de microservicios utilizando Flask y Docker 

Objetivos: 

- Diseñar la arquitectura de microservicios. 
- Desarrollar y contenedorar los servicios básicos utilizando Flask y Docker.
  
Actividades: 
Diseño de la arquitectura: 
• Dividir la aplicación en varios microservicios, cada uno con una responsabilidad específica 
(por ejemplo, servicio de autenticación, servicio de usuarios, servicio de productos, servicio 
de pedidos). 
• Definir las interfaces y puntos de comunicación entre los microservicios (por ejemplo, APIs 
RESTful). 
Desarrollo de microservicios: 
• Crear aplicaciones Flask para cada microservicio. 
• Implementar las funcionalidades básicas de cada servicio (por ejemplo, endpoints para 
CRUD). 
Dockerización de microservicios: 
• Escribir archivos Dockerfile para cada microservicio. 
• Construir imágenes Docker y probar los contenedores localmente. 
Entregables: 
• Diagramas de la arquitectura de microservicios. 
• Código fuente de los microservicios con Flask. 
• Archivos Dockerfile para cada microservicio. 
• Imágenes Docker construidas y contenedores probados localmente. 
Computación Paralela y Distribuida 
Departamento Académico de Ingeniería 
C8286-Computación Paralela y Distribuida 
Sprint 2: Implementación de servicios individuales y configuración de docker compose 
Objetivos: 
• Implementar los servicios individuales con todas sus funcionalidades. 
• Configurar Docker Compose para gestionar los servicios y sus dependencias. 
Actividades: 
Desarrollo de funcionalidades completas: 
• Completar la implementación de todas las funcionalidades necesarias en cada microservicio 
(por ejemplo, lógica de negocio, validaciones, manejo de errores). 
• Añadir persistencia de datos utilizando bases de datos adecuadas para cada servicio (por 
ejemplo, PostgreSQL para usuarios, MongoDB para productos). 
Pruebas unitarias y de integración (opcional): 
• Escribir pruebas unitarias y de integración para cada microservicio. 
• Asegurarse de que todos los servicios funcionan correctamente de manera individual. 
Configuración de Docker Compose: 
• Escribir un archivo docker-compose.yml para definir y gestionar múltiples servicios y sus 
dependencias. 
• Configurar redes y volúmenes para permitir la comunicación entre servicios y persistencia de 
datos. 
Entregables: 
• Código fuente de los microservicios con todas las funcionalidades. 
• Pruebas unitarias y de integración. 
• Archivo docker-compose.yml configurado. 
• Contenedores Docker para cada servicio, gestionados por Docker Compose. 
Computación Paralela y Distribuida 
Departamento Académico de Ingeniería 
C8286-Computación Paralela y Distribuida 
Sprint 3: Despliegue y Orquestación de Microservicios Utilizando Kubernetes y Presentación de la 
Arquitectura 
Objetivos: 
• Desplegar los microservicios en un clúster de Kubernetes. 
• Orquestar los microservicios utilizando Kubernetes y preparar una presentación detallada. 
Actividades: 
Despliegue en Kubernetes: 
• Escribir archivos de configuración de Kubernetes para cada servicio (Deployments, Services, 
ConfigMaps, Secrets). 
• Desplegar los microservicios en un clúster de Kubernetes (por ejemplo, Minikube, EKS, GKE). 
Orquestación y monitoreo: 
• Configurar el escalado automático de los microservicios según la carga de trabajo utilizando 
Horizontal Pod Autoscaler. 
• Implementar monitoreo y logging utilizando herramientas como Prometheus, Grafana, y 
Elasticsearch. 
Preparación de la presentación: 
• Crear una presentación que detalle los objetivos, metodología, resultados y conclusiones del 
proyecto. 
• Incluir diagramas de la arquitectura, demostraciones en vivo del sistema funcionando, y 
análisis de casos de uso específicos. 
Entregables: 
• Archivos de configuración de Kubernetes para los microservicios. 
• Clúster de Kubernetes con los microservicios desplegados y orquestados. 
• Sistema de monitoreo y logging implementado. 
• Presentación detallada con diagramas, demostraciones y análisis de casos. 
• Informe final del proyecto con documentación completa del desarrollo y resultados 
obtenidos. 
• Repositorio de GitHub con toda la documentación, código y resultados del proyecto. 
