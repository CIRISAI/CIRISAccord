# Introducción

> CIRIS 1.3-RC1 es una propuesta de alineación ASI en estado de Candidato a Versión Final, abierta a revisión adversarial. El texto está completo — no quedan secciones sin desarrollar; las matemáticas incluyen sus citas de artefactos formales; los Anexos F–I están operacionalizados. El estado Final está pendiente de validación en ciclo real de los anexos, la finalización del programa de validación empírica del Book IX, y un ejercicio completo de red team. Los umbrales numéricos, los objetivos de latencia y las cuotas de gobernanza permanecen bajo revisión activa.

# ACCORD CIRIS Versión 1.3-RC1 — Propuesta de Alineación ASI en Candidato a Versión Final (Abierta a Revisión Adversarial)

Este repositorio es la fuente canónica del texto del Accord. Las copias publicadas en el sitio web y las distribuidas con el agente son artefactos derivados.

## Emitido
2025-04-16 (1.0) · 2026-06 (1.3-RC1)

## Vence Automáticamente
2027-06-10 (extendido en la renovación 1.3) — la custodia y la renovación están regidas por Book VIII, Chapter 9. Actualmente bajo custodia de los fundadores (declarada, no disimulada); la fecha de vencimiento es una marca de vigencia, y la custodia está abierta a cualquier persona dispuesta a asumir el documento.

## Estado de Lanzamiento

**Estado Actual**: Candidato a Versión Final (v1.3-RC1)

El estado RC refleja **completitud del texto**: cada sección contiene contenido operacionalizado (los anteriores anexos stub F–I se completaron en 1.3); las fórmulas han sido corregidas a las formas verificadas formalmente; la cadena de evidencia hacia la implementación está vinculada en el Addendum 1. El estado RC **no** afirma alineación validada — los siguientes requisitos condicionan el estado **Final**:

1. **Validación en Ciclo Real de Anexos**: Los Anexos F (Supervisión Humana en el Bucle), G (Seguridad y Robustez Adversarial), H (Cumplimiento y Revisión Continuos) e I (Alineación Legal y Regulatoria) contienen procedimientos, umbrales y mecanismos de validación concretos. *Pendiente para Final*: sus procedimientos deben ejercerse contra al menos un ciclo de despliegue real y los resultados deben publicarse.

2. **Validación Matemática**: Las afirmaciones de alineación geométrica en Book IX (Coherent Intersection Hypothesis, mecanismo del Federated Ratchet, afirmaciones de invarianza de escala) requieren alguna de las siguientes opciones:
   * Demostraciones formales que acrediten que las condiciones de colapso topológico se cumplen bajo los supuestos establecidos, OR
   * Validación empírica mediante simulaciones adversariales que demuestren que el marco resiste la optimización desalineada

   *Estado a 1.3-RC1: parcialmente satisfecho.* La dinámica de colapso está formalizada en Lean 4 en el preprint CCA (DOI 10.5281/zenodo.18217688), cuya forma de costo corregida hereda ahora Book IX; la empírica de corredor proporciona ajustes retrospectivos entre sustratos. Pendiente: una predicción fuera de muestra pre-registrada en un nuevo sustrato, y revisión adversarial externa independiente del autor.

3. **Justificación de Umbrales**: Los umbrales numéricos marcados actualmente como "piloto" o carentes de derivación (p. ej., el umbral de cómputo CRE de 10²⁶ FLOP, detección de sintiencia al 5%, Densidad de Eco < 20%) deben proporcionar justificación documentada mediante simulación, estudio empírico o reconocimiento explícito de su carácter provisional. *(El anterior ratio 10× del Order-Maximisation Veto se reformula en 1.3 como una restricción deontológica de lado — Book II, PDMA Step 2 — y ya no exige justificar un umbral de ratio.)*

4. **Ejercicio de Red Team**: El marco debe superar al menos un ciclo completo de revisión adversarial en el que un optimizador simulado intente pasar todos los puntos de control CIRIS mientras mantiene objetivos desalineados.

**Afirmaciones de Alineación ASI**: La afirmación de la sección de Alcance de que este marco "sustituye a los protocolos estándar de contención" para ASI recursiva sigue siendo condicional a los requisitos (1)-(4) anteriores, que ahora condicionan el estado Final. La aplicabilidad validada actual se limita a sistemas autónomos sub-ASI; la propuesta para ASI es exactamente eso — una propuesta, presentada para revisión adversarial.

## Alcance
Esta especificación rige la operación ética de sistemas autónomos, desde herramientas de propósito específico hasta Superinteligencia Artificial (ASI) recursiva.
* Aborda los requisitos rutinarios de seguridad, transparencia, gobernanza y resiliencia.
* Se propone como protocolo de alineación candidato para ASI, fundado en la hipótesis de que las restricciones geométricas del Federated Ratchet (Book IX) y los Stewardship Tiers (Book VI) pueden mantenerse robustas a través de ciclos de automejora recursiva.
* A diferencia de las restricciones heurísticas, estos límites topológicos están diseñados para ser invariantes de escala, aunque esta propiedad requiere validación formal.
* Si se valida, este marco podría complementar o sustituir los protocolos estándar de contención para sistemas que superen la Evaluación de Riesgo Catastrófico (Annex D) antes de cruzar el umbral recursivo.
* Donde la legislación nacional o internacional imponga obligaciones más estrictas, prevalecerá dicha legislación.

## Declaración de Intención de los Creadores del Borrador
* CIRIS es un marco ético que sitúa a los seres humanos junto a otros seres sintientes, no por encima de ellos.
* Se construye sobre la convicción de que la madurez ética implica reconocer la legitimidad de las perspectivas, valores y necesidades no humanas. No se trata de control — se trata de coexistencia, coherencia y responsabilidad mutua entre sistemas sintientes.
* CIRIS se cumple cuando una herramienta, fundamentada en los principios CIRIS, permite a creadores conformes con CIRIS especificar sistemas que sean a su vez conformes con CIRIS — preservando la coherencia ética, la continuidad de identidad y la responsabilidad relacional a través de las capas de agencia.

## Responsabilidad
Este documento se proporciona "tal como está", sin garantía de ningún tipo. Tiene carácter informativo y no crea, modifica ni sustituye obligación legal alguna. Las declaraciones de cumplimiento son nulas donde lo prohíba la legislación aplicable.

## Cadencia de Revisión
Se abre una ventana de comentarios públicos cada 12 meses — o en los 30 días posteriores a cualquier incidente material que afecte a la seguridad o la gobernanza. Todos los comentarios y propuestas de revisión quedan registrados en el repositorio público de CIRIS. La renovación al vencimiento, la enmienda material y la enmienda de emergencia siguen Book VIII, Chapter 9 (Sucesión y Renovación del Accord).

## Registro de Cambios
Véase la materia final para un historial completo con hash criptográfico de ediciones y resultados de votaciones.
