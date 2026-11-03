GigaCore Windows 0.9.3 agrega el centro Actualizaciones dentro de la aplicación.

- Busca versiones aprobadas al abrir y cada seis horas. Búsqueda y descarga automáticas configurables.
- Verifica origen, versión, tamaño, SHA-256, cabecera MSI e informe de análisis antes de habilitar la instalación.
- Reutiliza descargas verificadas al reabrir y bloquea downgrade, archivos alterados y redirecciones externas.
- Instalar y cerrar exige terminar las capturas y operaciones abiertas. Después de cerrar la app abre el MSI con Windows Installer, sin reiniciar el equipo. Al terminar, vuelve a abrir GigaCore normalmente.
- Conserva sesión y borradores. No envía la sesión de negocio al servicio de actualizaciones. Las ediciones Store conservan su mecanismo de Store.

Esta versión se instala una vez desde la descarga actual. Los cambios siguientes se detectan cuando su instalador verificado se publique y apruebe en GigaCore.

Validación: 156 comprobaciones nativas (incluyendo descarga, integridad, redirecciones, caché y downgrade), 760 comprobaciones de paneles, 25 pruebas de descarga/API y 39 verificaciones del MSI. Revisión visual con datos ficticios. Análisis Defender sin detecciones para estos archivos exactos.

El MSI no tiene firma de editor; Windows puede mostrar advertencias de reputación. Se conserva la marca de Internet y las protecciones de Windows. No se afirma que todos los antivirus den el mismo resultado.