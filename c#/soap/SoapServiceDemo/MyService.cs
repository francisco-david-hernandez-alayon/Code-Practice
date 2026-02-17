public class MyService : IMyService
{
    public string SayHello(string name)
    {
        return $"Hola {name}, respuesta desde SOAP!";
    }
}
