using System.Collections.Generic;
using Pulumi;
using Random = Pulumi.Random;

return await Deployment.RunAsync(() => 
{
    var foo = new Random.RandomPet("foo", new()
    {
    }, new CustomResourceOptions
    {
        RetainOnDelete = true,
    });

});

