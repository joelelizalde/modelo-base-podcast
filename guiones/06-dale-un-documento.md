# Guiones · Modelo Base

## Episodio 06 · Dale un documento, no le enseñes a adivinar

**Duración:** 6:00

**ANA:** Joel, mi asistente inventa cosas sobre los productos de la empresa. Ya le puse en el prompt que no invente.

**JOEL:** ¿Y qué pasó?

**ANA:** Inventó menos, pero siguió inventando.

**JOEL:** Claro. Le pediste que recordara algo que nunca supo.

**ANA:** Entonces, ¿cómo le enseño?

**JOEL:** No le enseñas. Le das el documento en el momento. Eso es RAG.

**ANA:** Recuperación, aumento, generación.

**JOEL:** Recuperar los fragmentos relevantes, aumentarlos con la pregunta y generar la respuesta usando esa evidencia.

**ANA:** Suena simple.

**JOEL:** Simple en el diagrama. En la práctica tiene cinco decisiones que pueden arruinarlo.

**ANA:** Vamos una por una.

**JOEL:** Primero, el troceado. Partes los documentos en fragmentos. Si son muy grandes, metes ruido. Si son muy pequeños, pierdes contexto.

**ANA:** ¿Cuál es el tamaño correcto?

**JOEL:** Depende del documento. Para políticas, párrafos con algo de solapamiento. Para tablas, por fila o por sección. No hay un número universal.

**ANA:** ¿Y el solapamiento?

**JOEL:** Repetir un poco del final en el siguiente fragmento para no cortar una idea a la mitad. Suficiente para mantener continuidad, no tanto como para duplicar el costo.

**ANA:** Segundo.

**JOEL:** Los metadatos. Cada fragmento debe saber de dónde viene: documento, versión, fecha, sección, permiso. Sin metadatos no puedes citar ni filtrar por vigencia.

**ANA:** Y sin citar, el usuario no confía.

**JOEL:** Y tú no puedes auditar. Un RAG sin citas es un generador de rumores con buena ortografía.

**ANA:** Tercero: la búsqueda.

**JOEL:** Aquí hay una pelea. Búsqueda dispersa contra búsqueda densa.

**ANA:** Traduce.

**JOEL:** La dispersa, como BM25, busca términos exactos y les da peso por rareza. La densa usa embeddings: convierte texto en vectores y busca significado parecido.

**ANA:** La densa suena más moderna.

**JOEL:** Y por eso la gente la usa para todo. Pero si buscas el código de error E-4012, la búsqueda por significado puede devolver E-4013 porque «se parecen».

**ANA:** Y el usuario recibe la respuesta equivocada.

**JOEL:** Con mucha confianza. Para códigos, nombres propios y números, la búsqueda exacta suele ganar.

**ANA:** Entonces uso las dos.

**JOEL:** Híbrida. Y después un reranker que ordene los candidatos con más cuidado. Es una de las mejoras más rentables de un RAG.

**ANA:** Cuarto: el agente.

**JOEL:** Un agente no es un prompt largo. Es un sistema que razona, actúa y observa. Decide usar una herramienta, ve el resultado y ajusta.

**ANA:** ¿Y la memoria?

**JOEL:** La memoria no es un archivo infinito. Es una decisión sobre qué recordar, cuánto tiempo y con qué permiso.

**ANA:** Suena a producto, otra vez.

**JOEL:** Todo esto es producto. La tecnología es la parte fácil.

**ANA:** Quinto: la evaluación.

**JOEL:** La más importante. Cuando un RAG responde mal, no cambies el prompt todavía. Primero averigua en qué etapa falló.

**ANA:** ¿Cómo?

**JOEL:** Separa recuperación y generación. ¿El fragmento correcto estaba entre los recuperados? Si no estaba, el problema es la búsqueda. Si estaba y la respuesta lo ignoró, el problema es la generación.

**ANA:** Y si estaba, lo usó, pero lo interpretó mal.

**JOEL:** Entonces es fidelidad: la respuesta no se sostiene en la fuente. Eso se mide aparte de la relevancia.

**ANA:** Dame un ejemplo completo.

**JOEL:** Un cliente pregunta por qué su factura subió. El sistema recupera la política de precios, pero también un comunicado viejo. El modelo mezcla las dos y responde con la tarifa anterior.

**ANA:** ¿Dónde falló?

**JOEL:** En los metadatos y en el filtro de vigencia. Dos documentos contradictorios, ninguno marcado como obsoleto. El modelo no tenía forma de saber cuál mandaba.

**ANA:** Le pedimos criterio que no tenía.

**JOEL:** Le pedimos que resolviera un problema de datos con lenguaje.

**ANA:** Error típico.

**JOEL:** Añadir más documentos cuando el problema es la recuperación. Si el fragmento correcto nunca entra al contexto, más documentos solo añaden ruido.

**ANA:** ¿Y la solución?

**JOEL:** Medir recall de recuperación. Si el documento correcto no aparece en el top cinco, ningún prompt lo va a salvar.

**ANA:** Cierre.

**JOEL:** Que RAG no es magia. Es evidencia: traer la fuente correcta y obligar a la respuesta a sostenerse en ella.

**ANA:** La frase.

**JOEL:** Si tu modelo no sabe algo, no le enseñes a adivinar. Dale el documento.

**ANA:** Módulo seis: RAG y agentes. Enlace en las notas.

**JOEL:** En el próximo: por qué el ajuste fino casi nunca es la primera opción.
