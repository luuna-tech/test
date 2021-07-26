# Ejercicio para DevOps @ Zebrands

## Instrucciones

 1. Crear una API REST simple y que sea desplegada sobre Kubernetes en AWS.
 2. Tanto los códigos de la API y del despliegue de esta deben ser publicados en un repositorio en Github.
 3. Deberá incluir un `Readme` donde explique su solución, además de incluir las instrucciones para tener acceso a la API desplegada.
 4. Tendrá 72 horas para completar y enviar la solución.


## Restricciones Técnicas

 - Para la API REST puede ocupar cualquier lenguaje de programación y/o framework.
 - La API REST debe hacer uso de una base de datos y esta también debe ser desplegada en Kubernetes.
 - Se utilizará Git para el control de versiones.
 - La aplicación debe ser desplegada en Kubernetes.
 - Los manifiestos para el despliegue en Kubernetes deben estar incluídos en el repositorio.


### Sobre la API REST

Crear una API REST que permita mantener un catálogo simple de productos. Un producto tiene la siguiente definición:
```yaml
Product:
    - sku
    - name
    - brand
    - model
    - price
    - description
```
Adicionalmente la aplicación tendrá la existencia de un tipo de usuario `Admin`, que pueden hacer CRUD sobre los productos.

- La aplicación puede ser desarrollada en cualquier lenguaje de programación.
- La aplicación debe estar documentada, tanto su uso como su despliegue.
- La aplicación debe hacer uso de una base de datos.


### Sobre el despliegue en Kubernetes

 - Si no tiene posibilidad de crear un cluster Kubernetes, considere utilizar minikube en una instancia EC2.
 - Utilizar una herramienta de Infraetructura como código (IaC) para el levantamiento de Kubernetes y los recursos necesarios. Puntos extras si usa Terraform.
 - La aplicación debe estar expuesta usando un servicio o un `ingress controller`.
 - Incluir consideraciones de logging y observabilidad.
 - Opcionalmente puede incluir un pipeline de CI/CD (muy recomendable)
 - Puntos extras si el despliegue tiene consideraciones de seguridad.
