# Guiones · Modelo Base

## Episodio 10 · Lo que no se mide no se mejora

**Duración:** 6:09

**ANA:** Joel, ya tengo el modelo, el RAG y hasta un adaptador. ¿Ahora qué?

**JOEL:** Ahora construyes el sistema que los usa. Que es distinto.

**ANA:** ¿No era eso lo que veníamos haciendo?

**JOEL:** Lo veníamos diseñando. Ahora hay que hacerlo observable. Y ahí se cae la mitad de los proyectos.

**ANA:** Porque funciona en tu laptop.

**JOEL:** Porque funciona en tu laptop, con tus tres preguntas y sin nadie mirando.

**ANA:** Empecemos por la arquitectura.

**JOEL:** Primero el contexto. Qué información entra, de dónde viene, con qué permiso y con qué vigencia. Si esa decisión está mal, el mejor modelo no la arregla.

**ANA:** Después, los guardrails.

**JOEL:** De entrada y de salida. Entrada: validar formato, bloquear instrucciones maliciosas, limitar tamaño. Salida: revisar datos personales, afirmaciones peligrosas, formato.

**ANA:** ¿Y el enrutador?

**JOEL:** Un componente que decide qué camino toma cada solicitud. Modelo pequeño, modelo grande, búsqueda, regla directa. Ahorra costo y agrega complejidad. Solo vale la pena si puedes medirlo.

**ANA:** Llegamos a la caché.

**JOEL:** Caché de respuestas y caché de contexto. La primera evita llamadas repetidas. La segunda evita reprocesar el mismo prompt. Y hay que aislar por usuario: una caché mal separada filtra datos.

**ANA:** Eso es un incidente de seguridad, no una optimización.

**JOEL:** Exacto. La caché es infraestructura, pero también es una decisión de privacidad.

**ANA:** Hablemos de observabilidad.

**JOEL:** Lo que no se mide no se puede mejorar. Y lo que se mide mal se empeora con confianza.

**ANA:** ¿Qué se registra?

**JOEL:** Modelo, versión del prompt, tokens de entrada y salida, costo, latencia, resultado de los guardrails y, si hay herramientas, la traza completa.

**ANA:** La traza.

**JOEL:** El recorrido de la solicitud: qué se recuperó, qué herramienta se llamó, qué devolvió, dónde falló. Sin traza, diagnosticar es adivinar.

**ANA:** ¿Y no es mucha información?

**JOEL:** Es mucha y hay que tratarla con cuidado. Datos personales fuera, retención limitada, acceso restringido. Pero sin registro no hay mejora.

**ANA:** Pasemos a la orquestación.

**JOEL:** Una aplicación real no hace una llamada. Coordina recuperar, generar, validar y actuar. Y decide qué pasa cuando algo falla.

**ANA:** El orden importa.

**JOEL:** Mucho. Si validas antes de recuperar, puedes bloquear una consulta que era legítima. Si actúas antes de validar, puedes ejecutar algo irreversible.

**ANA:** ¿Y el estado?

**JOEL:** El estado no es un historial infinito. Es lo que el sistema necesita recordar para la siguiente decisión. Todo lo demás es ruido que cuesta tokens.

**ANA:** ¿Paralelizar?

**JOEL:** Lo independiente. Si tienes que recuperar de tres fuentes, no las hagas en serie. Pero si una depende de otra, paralelizar rompe la lógica.

**ANA:** Llegamos al feedback.

**JOEL:** El feedback de tus usuarios no es la verdad. Es una señal con sesgos.

**ANA:** ¿Qué tipo de sesgos?

**JOEL:** El de selección: responde quien tuvo una experiencia extrema. El de conveniencia: es más fácil dar pulgar abajo que explicar. Y el de poder: tus usuarios más técnicos usan funciones que el resto ni conoce.

**ANA:** Dame un ejemplo.

**JOEL:** Un equipo recibe cien comentarios al mes. El ochenta por ciento vienen del cinco por ciento de usuarios, casi todos avanzados. Construyen la siguiente función para ellos y el resto sigue esperando lo básico.

**ANA:** El feedback distorsiona el roadmap.

**JOEL:** Lo distorsiona si lo tratas como voto. Lo informa si lo cruzas con datos de uso.

**ANA:** ¿Qué tipos de feedback existen?

**JOEL:** Directo: pulgares, encuestas, comentarios. Indirecto: si el usuario reformula, copia la respuesta o abandona. Automático: evaluaciones que corren en producción con una muestra.

**ANA:** Los tres juntos.

**JOEL:** Los tres, con pesos distintos. Y una pregunta de control: ¿quién no está respondiendo?

**ANA:** Los que se fueron.

**JOEL:** Los que se fueron son la señal más valiosa y la más difícil de conseguir.

**ANA:** Error típico.

**JOEL:** Construir tableros que nadie usa para decidir. Métricas bonitas, reuniones semanales, cero cambios.

**ANA:** ¿Cómo se evita?

**JOEL:** Cada métrica debe tener un dueño y una acción asociada. Si sube o baja, ¿qué hacemos distinto? Si la respuesta es «nada», la métrica sobra.

**ANA:** Cierre de temporada.

**JOEL:** Que la arquitectura no es un diagrama. Es un conjunto de decisiones sobre contexto, límites, costo y error.

**ANA:** Y la frase.

**JOEL:** El sistema aprende si tú aprendes de él.

**ANA:** Módulo diez: arquitectura y feedback. Enlace en las notas.

**JOEL:** En el próximo y último episodio: las cinco decisiones que resumen toda la temporada.
