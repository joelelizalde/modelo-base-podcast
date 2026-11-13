# Guiones · Modelo Base

## Episodio 08 · Datos sucios, modelo confiado

**Duración:** 6:02

**ANA:** Joel, compré un dataset de un millón de filas. ¿Ahora sí tengo un buen modelo?

**JOEL:** Depende de cuántas de esas filas puedes defender.

**ANA:** Un millón es un millón.

**JOEL:** Un millón de errores también es un millón.

**ANA:** Siempre igual.

**JOEL:** Porque el volumen es la métrica más fácil de presumir y la menos útil para decidir.

**ANA:** Entonces, ¿qué hace bueno a un dataset?

**JOEL:** Tres cosas: corrección, consistencia y cobertura. Y ninguna se mide en gigabytes.

**ANA:** Corrección es que los datos sean ciertos.

**JOEL:** O al menos, que sean la mejor aproximación disponible. Y que el error esté medido, no escondido.

**ANA:** Consistencia es que no se contradigan.

**JOEL:** Dos ejemplos iguales con etiquetas distintas destruyen la señal. El modelo aprende ruido y lo repite con seguridad.

**ANA:** Y cobertura.

**JOEL:** Que represente los casos que van a aparecer en producción. No solo los fáciles. Los raros, los límites, los que duelen.

**ANA:** ¿Cómo se audita?

**JOEL:** Por subgrupo. No mires el promedio del dataset. Mira el rendimiento en cada tipo de caso: idioma, canal, longitud, cliente nuevo contra recurrente.

**ANA:** Porque el promedio esconde.

**JOEL:** El promedio es el mejor escondite del sesgo.

**ANA:** Hablemos de anotación.

**JOEL:** Aquí se comete el error más caro: escalar sin una guía clara. Si diez personas etiquetan sin criterio común, obtienes diez criterios.

**ANA:** Y el modelo aprende el promedio de los diez.

**JOEL:** Aprende la inconsistencia. Por eso la guía va antes de escalar, no después.

**ANA:** ¿Y cómo sé si la guía funciona?

**JOEL:** Midiendo el acuerdo entre anotadores. Si dos personas capacitadas no coinciden en el mismo caso, el problema no es el modelo: es la definición.

**ANA:** Eso es incómodo.

**JOEL:** Es incómodo y es información. Un desacuerdo alto te dice que tu etiqueta es ambigua.

**ANA:** Llegamos a los datos sintéticos.

**JOEL:** La promesa: generar datos con IA es barato. La realidad: no es gratis.

**ANA:** ¿Por qué?

**JOEL:** Porque pagas generación, revisión y riesgo. Si no revisas, entrenas al modelo con sus propios errores. Y el error se amplifica.

**ANA:** Colapso del modelo.

**JOEL:** Es uno de los riesgos. Otro es la pérdida de diversidad: el modelo sintético tiende a repetir estilos y a cubrir menos casos raros.

**ANA:** Entonces no sirven.

**JOEL:** Sirven para aumentar cobertura, para casos que no puedes conseguir, para preentrenar un formato. No sirven como sustituto ciego de datos reales.

**ANA:** ¿Y la destilación?

**JOEL:** Usar un modelo grande para generar respuestas y entrenar uno pequeño. Funciona, pero el pequeño imita al grande, incluidos sus sesgos y sus errores.

**ANA:** O sea, hereda la personalidad.

**JOEL:** Hereda la personalidad y los puntos ciegos. Si el grande se equivoca en un caso, el pequeño lo aprende.

**ANA:** Pasemos al procesamiento.

**JOEL:** De crudo a reproducible. Limpiar, normalizar, deduplicar, separar y documentar. Cada paso con una versión.

**ANA:** ¿Por qué reproducible?

**JOEL:** Porque dentro de seis meses alguien va a preguntar de dónde salió esa métrica. Si no puedes reconstruir el dataset, no puedes defender el resultado.

**ANA:** ¿Y la duplicación?

**JOEL:** Es la fuga más común. Si una fila está en entrenamiento y en prueba, el modelo la vio. Parece brillante y no lo es.

**ANA:** Dame un ejemplo.

**JOEL:** Un modelo de soporte con noventa y ocho por ciento en validación. En producción, sesenta. Al revisar, había conversaciones duplicadas entre los dos conjuntos.

**ANA:** Se memorizó las respuestas.

**JOEL:** Se memorizó el examen. No aprendió a resolver.

**ANA:** ¿Cómo se evita?

**JOEL:** Deduplicar antes de separar, y separar por grupo, no por fila. Si un cliente tiene diez conversaciones, todas van al mismo lado.

**ANA:** Privacidad.

**JOEL:** En el pipeline, no al final. Quitar datos personales antes de que entren al entrenamiento. Y registrar qué se eliminó.

**ANA:** Error típico.

**JOEL:** Medir el dataset en tamaño. «Tenemos dos terabytes». Bien. ¿Cuántos casos únicos, corregidos y cubriendo los límites?

**ANA:** Casi nadie sabe.

**JOEL:** Casi nadie. Y por eso los modelos fallan en los casos que nunca se recolectaron.

**ANA:** Cierre.

**JOEL:** Que un dataset no se mide en gigabytes. Se mide por las decisiones que puedes defender con él.

**ANA:** La frase.

**JOEL:** Si no puedes explicar cómo se etiquetó un caso difícil, no tienes datos. Tienes material.

**ANA:** Módulo ocho: ingeniería de datasets. Enlace en las notas.

**JOEL:** En el próximo: por qué la latencia promedio te está mintiendo.
