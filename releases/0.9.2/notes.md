GigaCore Windows 0.9.2 recuerda la sesión al cerrar y volver a abrir la aplicación, también para Administración.

- Guarda solamente la sesión ya autenticada con cifrado Windows DPAPI, ligada al usuario de Windows y al servidor. No guarda contraseñas ni secretos o códigos de 2FA.
- Verifica identidad, vigencia y permisos en el servidor antes de reanudar el trabajo.
- Cerrar la ventana conserva la sesión. Cerrar sesión elimina el acceso recordado. Se mantienen la revocación, caducidad y reautenticación de operaciones sensibles.
- Tras actualizar, inicia sesión una vez para activar la continuidad. Las siguientes aperturas restauran la sesión mientras siga vigente.

Validación: 125 comprobaciones nativas, 270 pruebas HTTP con datos ficticios (incluyendo reapertura y revocación de Ventas y Administración con 2FA), 760 comprobaciones de paneles y 39 verificaciones del MSI. Análisis de Microsoft Defender sin detecciones para los archivos exactos.

Cerrar GigaCore antes de instalar. MSI por usuario con actualización manual. El paquete no tiene firma de editor; Windows puede mostrar advertencias de reputación. No se desactiva ninguna protección y un análisis sin detecciones no garantiza el resultado de todos los antivirus.