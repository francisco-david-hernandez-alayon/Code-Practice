using CoreWCF;
using CoreWCF.Configuration;
using CoreWCF.Description;

var builder = WebApplication.CreateBuilder(args);
builder.WebHost.UseUrls("http://localhost:8000");

builder.Services.AddServiceModelServices();
builder.Services.AddServiceModelMetadata();

var app = builder.Build();

app.UseServiceModel(serviceBuilder =>
{
    serviceBuilder.AddService<MyService>();
    serviceBuilder.AddServiceEndpoint<MyService, IMyService>(
        new BasicHttpBinding(),
        "/MyService.svc");

    var smb = app.Services.GetRequiredService<ServiceMetadataBehavior>();
    smb.HttpGetEnabled = true;
});

app.Run();
