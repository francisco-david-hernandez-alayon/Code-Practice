## Crear Proyecto Web API: SoapServiceDemo
```
dotnet new web -n SoapServiceDemo
cd SoapServiceDemo
```

Instalar CoreWCF
```
dotnet add package CoreWCF.Http
dotnet add package CoreWCF.Primitives
dotnet add package CoreWCF.Metadata
```

Ejecutar
```
dotnet run
```

## Crear proyecto consola: SoapClientDemo
```
dotnet new console -n SoapClientDemo
cd SoapClientDemo
```
Agregar paquete
```
dotnet add package System.ServiceModel.Http
```

Ejecutar
```
dotnet run
```


