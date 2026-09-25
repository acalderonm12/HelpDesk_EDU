# Reporte de Evaluación Práctica - Parcial 2

Estudiante: Anyelo Gerardo Calderón Mazariegos  
Curso: Programación II  
Repositorio: 

---

## Registro Progresivo de Evidencias

### Ejercicio 1: Etiquetas y Encapsulamiento
- **Archivos modificados:** `app/models/entities.py`, `app/domain/errors.py`
- **Implementación:**
  - Se añadió la lista interna protegida `_tags` mediante `field(default_factory=list, init=False, repr=False)`.
  - Se expuso la propiedad `tags` que retorna una `tuple` de solo lectura (evitando reasignaciones directas como `ticket.tags = [...]`).
  - Se creó `add_tag(tag)` para limpiar espacios (`.strip().lower()`), validar etiquetas vacías lanzando `ValidationError` y evitar duplicados.
- **Pruebas:** Ejecutadas pruebas para verificar la inmutabilidad de la tupla y el rechazo de etiquetas vacías/duplicadas.