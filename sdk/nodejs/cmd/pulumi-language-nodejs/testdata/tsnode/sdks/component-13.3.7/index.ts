// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export * from "./componentCallable";
import { ComponentCallable } from "./componentCallable";

export { ComponentCustomRefInputOutputArgs } from "./componentCustomRefInputOutput";
export type ComponentCustomRefInputOutput = import("./componentCustomRefInputOutput").ComponentCustomRefInputOutput;
export const ComponentCustomRefInputOutput: typeof import("./componentCustomRefInputOutput").ComponentCustomRefInputOutput = null as any;
utilities.lazyLoad(exports, ["ComponentCustomRefInputOutput"], () => require("./componentCustomRefInputOutput"));

export { ComponentCustomRefOutputArgs } from "./componentCustomRefOutput";
export type ComponentCustomRefOutput = import("./componentCustomRefOutput").ComponentCustomRefOutput;
export const ComponentCustomRefOutput: typeof import("./componentCustomRefOutput").ComponentCustomRefOutput = null as any;
utilities.lazyLoad(exports, ["ComponentCustomRefOutput"], () => require("./componentCustomRefOutput"));

export { CustomArgs } from "./custom";
export type Custom = import("./custom").Custom;
export const Custom: typeof import("./custom").Custom = null as any;
utilities.lazyLoad(exports, ["Custom"], () => require("./custom"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "component:index:ComponentCallable":
                return new ComponentCallable(name, <any>undefined, { urn })
            case "component:index:ComponentCustomRefInputOutput":
                return new ComponentCustomRefInputOutput(name, <any>undefined, { urn })
            case "component:index:ComponentCustomRefOutput":
                return new ComponentCustomRefOutput(name, <any>undefined, { urn })
            case "component:index:Custom":
                return new Custom(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("component", "index", _module)
pulumi.runtime.registerResourcePackage("component", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:component") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
