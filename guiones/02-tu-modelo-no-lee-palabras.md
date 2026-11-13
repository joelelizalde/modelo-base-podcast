# Guiones · Modelo Base

## Episodio 02 · Tu modelo no lee palabras

**Duración:** 7:20

**ANA:** Joel, ayer le hice la misma pregunta dos veces al mismo modelo y me dio dos respuestas distintas. ¿Está roto?

**JOEL:** No. Está haciendo exactamente lo que le pediste.

**ANA:** Le pedí la verdad.

**JOEL:** Le pediste una continuación probable. No es lo mismo.

**ANA:** Explícame.

**JOEL:** Un modelo de lenguaje no consulta una base de datos. Calcula la siguiente pieza de texto más probable, la elige, y repite. Ese proceso tiene azar.

**ANA:** Entonces nunca voy a poder confiar en una respuesta.

**JOEL:** Puedes confiar en el sistema que construyes alrededor. Pero primero hay que entender la unidad con la que trabaja. Y no es la palabra.

**ANA:** ¿Es el token?

**JOEL:** El token. Tu modelo no lee palabras. Lee tokens.

**ANA:** ¿Y qué es un token?

**JOEL:** Una pieza de texto: a veces una palabra completa, a veces un pedazo. «Increíble» puede partirse en cuatro o cinco tokens. Un número largo puede partirse en varios.

**ANA:** ¿Por qué importa?

**JOEL:** Por tres cosas. La factura, la cobertura y lo que el modelo puede ver a la vez.

**ANA:** Empecemos por la factura.

**JOEL:** Cobran por token de entrada y por token de salida. Y el español suele gastar entre un veinte y un cincuenta por ciento más tokens que el inglés para el mismo contenido.

**ANA:** O sea que nuestra serie cuesta más en español.

**JOEL:** Sí. Y un contrato de cuarenta páginas puede ser sesenta mil tokens. Si lo mandas completo en cada pregunta, lo pagas completo en cada pregunta.

**ANA:** Aunque la respuesta sea «sí».

**JOEL:** Aunque la respuesta sea «sí». Por eso existe la recuperación: mandar solo los fragmentos relevantes.

**ANA:** Y la cobertura.

**JOEL:** La ventana de contexto. Es el máximo de tokens que el modelo puede considerar a la vez: entrada más salida. Si te pasas, truncas. Y truncar no avisa.

**ANA:** Suena a que se pierde información en silencio.

**JOEL:** Se pierde en silencio. Y el modelo sigue respondiendo con seguridad.

**ANA:** Qué tranquilizador.

**JOEL:** Por eso hay que medir. Un prompt que crece cada semana termina rompiendo algo.

**ANA:** Ahora lo del «banco». La palabra cambia según la frase.

**JOEL:** Ahí entra el transformer. La idea central es la atención: cada token mira a los demás y decide cuáles son relevantes para interpretarlo.

**ANA:** Como leer la sala antes de hablar.

**JOEL:** Buen ejemplo. En «fui al banco a sacar dinero», «banco» atiende a «dinero». En «me senté en el banco del parque», atiende a «parque». Mismo token, distinto significado.

**ANA:** ¿Y eso se aprende solo?

**JOEL:** Se aprende del texto. Nadie le enseña gramática; aprende patrones de uso. Por eso funciona en tantos idiomas y por eso también hereda los sesgos del texto.

**ANA:** Llegamos a la parte incómoda.

**JOEL:** Llegamos. Pero antes, una distinción que confunde a mucha gente: modelo base y modelo de instrucciones.

**ANA:** Yo pensaba que eran lo mismo.

**JOEL:** El modelo base solo completa texto. Si le pones «La capital de Francia es», dice «París». Útil, pero no es un asistente.

**ANA:** ¿Y el otro?

**JOEL:** Pasa por postentrenamiento. Primero ejemplos de instrucciones y respuestas, el llamado ajuste supervisado. Después, preferencias: humanos o modelos comparan respuestas y el modelo aprende cuál se acerca más a lo que queremos.

**ANA:** O sea, le enseñan modales.

**JOEL:** Le enseñan formato, tono y límites. No le enseñan tu empresa.

**ANA:** Volvemos al episodio uno.

**JOEL:** Volvemos. El postentrenamiento no le da conocimiento nuevo confiable. Le da conducta.

**ANA:** Entonces, si quiero que sepa de mis políticas, ¿no basta con afinarlo?

**JOEL:** No es la herramienta adecuada. Para conocimiento cambiante, recuperas. Para conducta estable, ajustas. Lo veremos en el episodio siete.

**ANA:** Quedamos en la aleatoriedad. ¿Puedo apagarla?

**JOEL:** Puedes reducirla. La temperatura controla cuánto se arriesga al elegir el siguiente token. Cerca de cero elige casi siempre lo más probable; más alta reparte probabilidad entre otras opciones.

**ANA:** Entonces con temperatura cero es determinista.

**JOEL:** Casi. No es una garantía. Cambia el hardware, cambia la versión del modelo, cambia el orden de las operaciones, y la misma entrada puede dar otra salida.

**ANA:** Eso rompe mis pruebas.

**JOEL:** Por eso las pruebas no comparan texto exacto. Comparan propiedades: ¿citó la fuente?, ¿respetó el formato?, ¿inventó una política? Es el tema del episodio tres.

**ANA:** Dame el error típico de este episodio.

**JOEL:** Comparar precios por token sin medir cuántos tokens gasta tu caso real. Dos modelos con tarifas parecidas pueden costar muy distinto según el tokenizador y la longitud de tus prompts.

**ANA:** ¿Y la solución?

**JOEL:** Mide. Toma cien consultas reales, cuenta tokens de entrada y salida, y calcula el costo por operación. No por millón de tokens: por respuesta que tu usuario recibe.

**ANA:** Por respuesta. Me gusta.

**JOEL:** Y si el prompt lleva el mismo contexto en todas las consultas, considera caché. Puede bajar el costo de forma importante.

**ANA:** Suena a optimización de verdad, no a comprar más GPU.

**JOEL:** Esa es la idea. La mayor parte del costo se decide antes de llamar al modelo.

**ANA:** Cierre. Si alguien se lleva una sola idea.

**JOEL:** Que el modelo no ve palabras ni significados. Ve tokens y probabilidades. Todo lo demás lo construyes tú.

**ANA:** Y la frase para repetir en una comida.

**JOEL:** La temperatura no es creatividad. Es una perilla de riesgo.

**ANA:** Módulo dos del curso: cómo funcionan los modelos base. Enlace en las notas.

**JOEL:** Y en el próximo episodio: por qué aprobar una respuesta no significa que sepas evaluarla.
