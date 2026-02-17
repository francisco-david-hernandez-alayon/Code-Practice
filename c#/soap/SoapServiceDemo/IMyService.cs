using CoreWCF;

[ServiceContract]
public interface IMyService
{
    [OperationContract]
    string SayHello(string name);
}
