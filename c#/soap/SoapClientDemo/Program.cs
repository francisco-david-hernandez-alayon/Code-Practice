using System;
using System.ServiceModel;

[ServiceContract]
public interface IMyService
{
    [OperationContract]
    string SayHello(string name);
}

class Program
{
    static void Main()
    {
        var binding = new BasicHttpBinding();
        var endpoint = new EndpointAddress("http://localhost:8000/MyService.svc");

        var factory = new ChannelFactory<IMyService>(binding, endpoint);
        var channel = factory.CreateChannel();

        var response = channel.SayHello("Carlos");

        Console.WriteLine(response);

        ((IClientChannel)channel).Close();
        factory.Close();
    }
}
