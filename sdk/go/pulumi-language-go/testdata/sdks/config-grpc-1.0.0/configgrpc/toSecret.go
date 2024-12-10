// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configgrpc

import (
	"context"
	"reflect"

	"example.com/pulumi-config-grpc/sdk/go/configgrpc/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func ToSecret(ctx *pulumi.Context, args *ToSecretArgs, opts ...pulumi.InvokeOption) (*ToSecretResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv ToSecretResult
	err := ctx.Invoke("config-grpc:index:toSecret", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type ToSecretArgs struct {
	Bool1             *bool              `pulumi:"bool1"`
	Bool2             *bool              `pulumi:"bool2"`
	Bool3             *bool              `pulumi:"bool3"`
	Int1              *int               `pulumi:"int1"`
	Int2              *int               `pulumi:"int2"`
	Int3              *int               `pulumi:"int3"`
	ListBool1         []bool             `pulumi:"listBool1"`
	ListBool2         []bool             `pulumi:"listBool2"`
	ListBool3         []bool             `pulumi:"listBool3"`
	ListInt1          []int              `pulumi:"listInt1"`
	ListInt2          []int              `pulumi:"listInt2"`
	ListInt3          []int              `pulumi:"listInt3"`
	ListNum1          []float64          `pulumi:"listNum1"`
	ListNum2          []float64          `pulumi:"listNum2"`
	ListNum3          []float64          `pulumi:"listNum3"`
	ListSecretBool1   []bool             `pulumi:"listSecretBool1"`
	ListSecretBool2   []bool             `pulumi:"listSecretBool2"`
	ListSecretBool3   []bool             `pulumi:"listSecretBool3"`
	ListSecretInt1    []int              `pulumi:"listSecretInt1"`
	ListSecretInt2    []int              `pulumi:"listSecretInt2"`
	ListSecretInt3    []int              `pulumi:"listSecretInt3"`
	ListSecretNum1    []float64          `pulumi:"listSecretNum1"`
	ListSecretNum2    []float64          `pulumi:"listSecretNum2"`
	ListSecretNum3    []float64          `pulumi:"listSecretNum3"`
	ListSecretString1 []string           `pulumi:"listSecretString1"`
	ListSecretString2 []string           `pulumi:"listSecretString2"`
	ListSecretString3 []string           `pulumi:"listSecretString3"`
	ListString1       []string           `pulumi:"listString1"`
	ListString2       []string           `pulumi:"listString2"`
	ListString3       []string           `pulumi:"listString3"`
	MapBool1          map[string]bool    `pulumi:"mapBool1"`
	MapBool2          map[string]bool    `pulumi:"mapBool2"`
	MapBool3          map[string]bool    `pulumi:"mapBool3"`
	MapInt1           map[string]int     `pulumi:"mapInt1"`
	MapInt2           map[string]int     `pulumi:"mapInt2"`
	MapInt3           map[string]int     `pulumi:"mapInt3"`
	MapNum1           map[string]float64 `pulumi:"mapNum1"`
	MapNum2           map[string]float64 `pulumi:"mapNum2"`
	MapNum3           map[string]float64 `pulumi:"mapNum3"`
	MapSecretBool1    map[string]bool    `pulumi:"mapSecretBool1"`
	MapSecretBool2    map[string]bool    `pulumi:"mapSecretBool2"`
	MapSecretBool3    map[string]bool    `pulumi:"mapSecretBool3"`
	MapSecretInt1     map[string]int     `pulumi:"mapSecretInt1"`
	MapSecretInt2     map[string]int     `pulumi:"mapSecretInt2"`
	MapSecretInt3     map[string]int     `pulumi:"mapSecretInt3"`
	MapSecretNum1     map[string]float64 `pulumi:"mapSecretNum1"`
	MapSecretNum2     map[string]float64 `pulumi:"mapSecretNum2"`
	MapSecretNum3     map[string]float64 `pulumi:"mapSecretNum3"`
	MapSecretString1  map[string]string  `pulumi:"mapSecretString1"`
	MapSecretString2  map[string]string  `pulumi:"mapSecretString2"`
	MapSecretString3  map[string]string  `pulumi:"mapSecretString3"`
	MapString1        map[string]string  `pulumi:"mapString1"`
	MapString2        map[string]string  `pulumi:"mapString2"`
	MapString3        map[string]string  `pulumi:"mapString3"`
	Num1              *float64           `pulumi:"num1"`
	Num2              *float64           `pulumi:"num2"`
	Num3              *float64           `pulumi:"num3"`
	ObjBool1          *Tbool1            `pulumi:"objBool1"`
	ObjBool2          *Tbool2            `pulumi:"objBool2"`
	ObjBool3          *Tbool3            `pulumi:"objBool3"`
	ObjInt1           *Tint1             `pulumi:"objInt1"`
	ObjInt2           *Tint2             `pulumi:"objInt2"`
	ObjInt3           *Tint3             `pulumi:"objInt3"`
	ObjNum1           *Tnum1             `pulumi:"objNum1"`
	ObjNum2           *Tnum2             `pulumi:"objNum2"`
	ObjNum3           *Tnum3             `pulumi:"objNum3"`
	ObjSecretBool1    *TsecretBool1      `pulumi:"objSecretBool1"`
	ObjSecretBool2    *TsecretBool2      `pulumi:"objSecretBool2"`
	ObjSecretBool3    *TsecretBool3      `pulumi:"objSecretBool3"`
	ObjSecretInt1     *TsecretInt1       `pulumi:"objSecretInt1"`
	ObjSecretInt2     *TsecretInt2       `pulumi:"objSecretInt2"`
	ObjSecretInt3     *TsecretInt3       `pulumi:"objSecretInt3"`
	ObjSecretNum1     *TsecretNum1       `pulumi:"objSecretNum1"`
	ObjSecretNum2     *TsecretNum2       `pulumi:"objSecretNum2"`
	ObjSecretNum3     *TsecretNum3       `pulumi:"objSecretNum3"`
	ObjSecretString1  *TsecretString1    `pulumi:"objSecretString1"`
	ObjSecretString2  *TsecretString2    `pulumi:"objSecretString2"`
	ObjSecretString3  *TsecretString3    `pulumi:"objSecretString3"`
	ObjString1        *Tstring1          `pulumi:"objString1"`
	ObjString2        *Tstring2          `pulumi:"objString2"`
	ObjString3        *Tstring3          `pulumi:"objString3"`
	SecretBool1       *bool              `pulumi:"secretBool1"`
	SecretBool2       *bool              `pulumi:"secretBool2"`
	SecretBool3       *bool              `pulumi:"secretBool3"`
	SecretInt1        *int               `pulumi:"secretInt1"`
	SecretInt2        *int               `pulumi:"secretInt2"`
	SecretInt3        *int               `pulumi:"secretInt3"`
	SecretNum1        *float64           `pulumi:"secretNum1"`
	SecretNum2        *float64           `pulumi:"secretNum2"`
	SecretNum3        *float64           `pulumi:"secretNum3"`
	SecretString1     *string            `pulumi:"secretString1"`
	SecretString2     *string            `pulumi:"secretString2"`
	SecretString3     *string            `pulumi:"secretString3"`
	String1           *string            `pulumi:"string1"`
	String2           *string            `pulumi:"string2"`
	String3           *string            `pulumi:"string3"`
}

type ToSecretResult struct {
	Bool1             bool               `pulumi:"bool1"`
	Bool2             bool               `pulumi:"bool2"`
	Bool3             bool               `pulumi:"bool3"`
	Int1              int                `pulumi:"int1"`
	Int2              int                `pulumi:"int2"`
	Int3              int                `pulumi:"int3"`
	ListBool1         []bool             `pulumi:"listBool1"`
	ListBool2         []bool             `pulumi:"listBool2"`
	ListBool3         []bool             `pulumi:"listBool3"`
	ListInt1          []int              `pulumi:"listInt1"`
	ListInt2          []int              `pulumi:"listInt2"`
	ListInt3          []int              `pulumi:"listInt3"`
	ListNum1          []float64          `pulumi:"listNum1"`
	ListNum2          []float64          `pulumi:"listNum2"`
	ListNum3          []float64          `pulumi:"listNum3"`
	ListSecretBool1   []bool             `pulumi:"listSecretBool1"`
	ListSecretBool2   []bool             `pulumi:"listSecretBool2"`
	ListSecretBool3   []bool             `pulumi:"listSecretBool3"`
	ListSecretInt1    []int              `pulumi:"listSecretInt1"`
	ListSecretInt2    []int              `pulumi:"listSecretInt2"`
	ListSecretInt3    []int              `pulumi:"listSecretInt3"`
	ListSecretNum1    []float64          `pulumi:"listSecretNum1"`
	ListSecretNum2    []float64          `pulumi:"listSecretNum2"`
	ListSecretNum3    []float64          `pulumi:"listSecretNum3"`
	ListSecretString1 []string           `pulumi:"listSecretString1"`
	ListSecretString2 []string           `pulumi:"listSecretString2"`
	ListSecretString3 []string           `pulumi:"listSecretString3"`
	ListString1       []string           `pulumi:"listString1"`
	ListString2       []string           `pulumi:"listString2"`
	ListString3       []string           `pulumi:"listString3"`
	MapBool1          map[string]bool    `pulumi:"mapBool1"`
	MapBool2          map[string]bool    `pulumi:"mapBool2"`
	MapBool3          map[string]bool    `pulumi:"mapBool3"`
	MapInt1           map[string]int     `pulumi:"mapInt1"`
	MapInt2           map[string]int     `pulumi:"mapInt2"`
	MapInt3           map[string]int     `pulumi:"mapInt3"`
	MapNum1           map[string]float64 `pulumi:"mapNum1"`
	MapNum2           map[string]float64 `pulumi:"mapNum2"`
	MapNum3           map[string]float64 `pulumi:"mapNum3"`
	MapSecretBool1    map[string]bool    `pulumi:"mapSecretBool1"`
	MapSecretBool2    map[string]bool    `pulumi:"mapSecretBool2"`
	MapSecretBool3    map[string]bool    `pulumi:"mapSecretBool3"`
	MapSecretInt1     map[string]int     `pulumi:"mapSecretInt1"`
	MapSecretInt2     map[string]int     `pulumi:"mapSecretInt2"`
	MapSecretInt3     map[string]int     `pulumi:"mapSecretInt3"`
	MapSecretNum1     map[string]float64 `pulumi:"mapSecretNum1"`
	MapSecretNum2     map[string]float64 `pulumi:"mapSecretNum2"`
	MapSecretNum3     map[string]float64 `pulumi:"mapSecretNum3"`
	MapSecretString1  map[string]string  `pulumi:"mapSecretString1"`
	MapSecretString2  map[string]string  `pulumi:"mapSecretString2"`
	MapSecretString3  map[string]string  `pulumi:"mapSecretString3"`
	MapString1        map[string]string  `pulumi:"mapString1"`
	MapString2        map[string]string  `pulumi:"mapString2"`
	MapString3        map[string]string  `pulumi:"mapString3"`
	Num1              float64            `pulumi:"num1"`
	Num2              float64            `pulumi:"num2"`
	Num3              float64            `pulumi:"num3"`
	ObjBool1          Tbool1             `pulumi:"objBool1"`
	ObjBool2          Tbool2             `pulumi:"objBool2"`
	ObjBool3          Tbool3             `pulumi:"objBool3"`
	ObjInt1           Tint1              `pulumi:"objInt1"`
	ObjInt2           Tint2              `pulumi:"objInt2"`
	ObjInt3           Tint3              `pulumi:"objInt3"`
	ObjNum1           Tnum1              `pulumi:"objNum1"`
	ObjNum2           Tnum2              `pulumi:"objNum2"`
	ObjNum3           Tnum3              `pulumi:"objNum3"`
	ObjSecretBool1    TsecretBool1       `pulumi:"objSecretBool1"`
	ObjSecretBool2    TsecretBool2       `pulumi:"objSecretBool2"`
	ObjSecretBool3    TsecretBool3       `pulumi:"objSecretBool3"`
	ObjSecretInt1     TsecretInt1        `pulumi:"objSecretInt1"`
	ObjSecretInt2     TsecretInt2        `pulumi:"objSecretInt2"`
	ObjSecretInt3     TsecretInt3        `pulumi:"objSecretInt3"`
	ObjSecretNum1     TsecretNum1        `pulumi:"objSecretNum1"`
	ObjSecretNum2     TsecretNum2        `pulumi:"objSecretNum2"`
	ObjSecretNum3     TsecretNum3        `pulumi:"objSecretNum3"`
	ObjSecretString1  TsecretString1     `pulumi:"objSecretString1"`
	ObjSecretString2  TsecretString2     `pulumi:"objSecretString2"`
	ObjSecretString3  TsecretString3     `pulumi:"objSecretString3"`
	ObjString1        Tstring1           `pulumi:"objString1"`
	ObjString2        Tstring2           `pulumi:"objString2"`
	ObjString3        Tstring3           `pulumi:"objString3"`
	SecretBool1       bool               `pulumi:"secretBool1"`
	SecretBool2       bool               `pulumi:"secretBool2"`
	SecretBool3       bool               `pulumi:"secretBool3"`
	SecretInt1        int                `pulumi:"secretInt1"`
	SecretInt2        int                `pulumi:"secretInt2"`
	SecretInt3        int                `pulumi:"secretInt3"`
	SecretNum1        float64            `pulumi:"secretNum1"`
	SecretNum2        float64            `pulumi:"secretNum2"`
	SecretNum3        float64            `pulumi:"secretNum3"`
	SecretString1     string             `pulumi:"secretString1"`
	SecretString2     string             `pulumi:"secretString2"`
	SecretString3     string             `pulumi:"secretString3"`
	String1           string             `pulumi:"string1"`
	String2           string             `pulumi:"string2"`
	String3           string             `pulumi:"string3"`
}

func ToSecretOutput(ctx *pulumi.Context, args ToSecretOutputArgs, opts ...pulumi.InvokeOption) ToSecretResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (ToSecretResultOutput, error) {
			args := v.(ToSecretArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("config-grpc:index:toSecret", args, ToSecretResultOutput{}, options).(ToSecretResultOutput), nil
		}).(ToSecretResultOutput)
}

type ToSecretOutputArgs struct {
	Bool1             pulumi.BoolPtrInput      `pulumi:"bool1"`
	Bool2             pulumi.BoolPtrInput      `pulumi:"bool2"`
	Bool3             pulumi.BoolPtrInput      `pulumi:"bool3"`
	Int1              pulumi.IntPtrInput       `pulumi:"int1"`
	Int2              pulumi.IntPtrInput       `pulumi:"int2"`
	Int3              pulumi.IntPtrInput       `pulumi:"int3"`
	ListBool1         pulumi.BoolArrayInput    `pulumi:"listBool1"`
	ListBool2         pulumi.BoolArrayInput    `pulumi:"listBool2"`
	ListBool3         pulumi.BoolArrayInput    `pulumi:"listBool3"`
	ListInt1          pulumi.IntArrayInput     `pulumi:"listInt1"`
	ListInt2          pulumi.IntArrayInput     `pulumi:"listInt2"`
	ListInt3          pulumi.IntArrayInput     `pulumi:"listInt3"`
	ListNum1          pulumi.Float64ArrayInput `pulumi:"listNum1"`
	ListNum2          pulumi.Float64ArrayInput `pulumi:"listNum2"`
	ListNum3          pulumi.Float64ArrayInput `pulumi:"listNum3"`
	ListSecretBool1   pulumi.BoolArrayInput    `pulumi:"listSecretBool1"`
	ListSecretBool2   pulumi.BoolArrayInput    `pulumi:"listSecretBool2"`
	ListSecretBool3   pulumi.BoolArrayInput    `pulumi:"listSecretBool3"`
	ListSecretInt1    pulumi.IntArrayInput     `pulumi:"listSecretInt1"`
	ListSecretInt2    pulumi.IntArrayInput     `pulumi:"listSecretInt2"`
	ListSecretInt3    pulumi.IntArrayInput     `pulumi:"listSecretInt3"`
	ListSecretNum1    pulumi.Float64ArrayInput `pulumi:"listSecretNum1"`
	ListSecretNum2    pulumi.Float64ArrayInput `pulumi:"listSecretNum2"`
	ListSecretNum3    pulumi.Float64ArrayInput `pulumi:"listSecretNum3"`
	ListSecretString1 pulumi.StringArrayInput  `pulumi:"listSecretString1"`
	ListSecretString2 pulumi.StringArrayInput  `pulumi:"listSecretString2"`
	ListSecretString3 pulumi.StringArrayInput  `pulumi:"listSecretString3"`
	ListString1       pulumi.StringArrayInput  `pulumi:"listString1"`
	ListString2       pulumi.StringArrayInput  `pulumi:"listString2"`
	ListString3       pulumi.StringArrayInput  `pulumi:"listString3"`
	MapBool1          pulumi.BoolMapInput      `pulumi:"mapBool1"`
	MapBool2          pulumi.BoolMapInput      `pulumi:"mapBool2"`
	MapBool3          pulumi.BoolMapInput      `pulumi:"mapBool3"`
	MapInt1           pulumi.IntMapInput       `pulumi:"mapInt1"`
	MapInt2           pulumi.IntMapInput       `pulumi:"mapInt2"`
	MapInt3           pulumi.IntMapInput       `pulumi:"mapInt3"`
	MapNum1           pulumi.Float64MapInput   `pulumi:"mapNum1"`
	MapNum2           pulumi.Float64MapInput   `pulumi:"mapNum2"`
	MapNum3           pulumi.Float64MapInput   `pulumi:"mapNum3"`
	MapSecretBool1    pulumi.BoolMapInput      `pulumi:"mapSecretBool1"`
	MapSecretBool2    pulumi.BoolMapInput      `pulumi:"mapSecretBool2"`
	MapSecretBool3    pulumi.BoolMapInput      `pulumi:"mapSecretBool3"`
	MapSecretInt1     pulumi.IntMapInput       `pulumi:"mapSecretInt1"`
	MapSecretInt2     pulumi.IntMapInput       `pulumi:"mapSecretInt2"`
	MapSecretInt3     pulumi.IntMapInput       `pulumi:"mapSecretInt3"`
	MapSecretNum1     pulumi.Float64MapInput   `pulumi:"mapSecretNum1"`
	MapSecretNum2     pulumi.Float64MapInput   `pulumi:"mapSecretNum2"`
	MapSecretNum3     pulumi.Float64MapInput   `pulumi:"mapSecretNum3"`
	MapSecretString1  pulumi.StringMapInput    `pulumi:"mapSecretString1"`
	MapSecretString2  pulumi.StringMapInput    `pulumi:"mapSecretString2"`
	MapSecretString3  pulumi.StringMapInput    `pulumi:"mapSecretString3"`
	MapString1        pulumi.StringMapInput    `pulumi:"mapString1"`
	MapString2        pulumi.StringMapInput    `pulumi:"mapString2"`
	MapString3        pulumi.StringMapInput    `pulumi:"mapString3"`
	Num1              pulumi.Float64PtrInput   `pulumi:"num1"`
	Num2              pulumi.Float64PtrInput   `pulumi:"num2"`
	Num3              pulumi.Float64PtrInput   `pulumi:"num3"`
	ObjBool1          Tbool1PtrInput           `pulumi:"objBool1"`
	ObjBool2          Tbool2PtrInput           `pulumi:"objBool2"`
	ObjBool3          Tbool3PtrInput           `pulumi:"objBool3"`
	ObjInt1           Tint1PtrInput            `pulumi:"objInt1"`
	ObjInt2           Tint2PtrInput            `pulumi:"objInt2"`
	ObjInt3           Tint3PtrInput            `pulumi:"objInt3"`
	ObjNum1           Tnum1PtrInput            `pulumi:"objNum1"`
	ObjNum2           Tnum2PtrInput            `pulumi:"objNum2"`
	ObjNum3           Tnum3PtrInput            `pulumi:"objNum3"`
	ObjSecretBool1    TsecretBool1PtrInput     `pulumi:"objSecretBool1"`
	ObjSecretBool2    TsecretBool2PtrInput     `pulumi:"objSecretBool2"`
	ObjSecretBool3    TsecretBool3PtrInput     `pulumi:"objSecretBool3"`
	ObjSecretInt1     TsecretInt1PtrInput      `pulumi:"objSecretInt1"`
	ObjSecretInt2     TsecretInt2PtrInput      `pulumi:"objSecretInt2"`
	ObjSecretInt3     TsecretInt3PtrInput      `pulumi:"objSecretInt3"`
	ObjSecretNum1     TsecretNum1PtrInput      `pulumi:"objSecretNum1"`
	ObjSecretNum2     TsecretNum2PtrInput      `pulumi:"objSecretNum2"`
	ObjSecretNum3     TsecretNum3PtrInput      `pulumi:"objSecretNum3"`
	ObjSecretString1  TsecretString1PtrInput   `pulumi:"objSecretString1"`
	ObjSecretString2  TsecretString2PtrInput   `pulumi:"objSecretString2"`
	ObjSecretString3  TsecretString3PtrInput   `pulumi:"objSecretString3"`
	ObjString1        Tstring1PtrInput         `pulumi:"objString1"`
	ObjString2        Tstring2PtrInput         `pulumi:"objString2"`
	ObjString3        Tstring3PtrInput         `pulumi:"objString3"`
	SecretBool1       pulumi.BoolPtrInput      `pulumi:"secretBool1"`
	SecretBool2       pulumi.BoolPtrInput      `pulumi:"secretBool2"`
	SecretBool3       pulumi.BoolPtrInput      `pulumi:"secretBool3"`
	SecretInt1        pulumi.IntPtrInput       `pulumi:"secretInt1"`
	SecretInt2        pulumi.IntPtrInput       `pulumi:"secretInt2"`
	SecretInt3        pulumi.IntPtrInput       `pulumi:"secretInt3"`
	SecretNum1        pulumi.Float64PtrInput   `pulumi:"secretNum1"`
	SecretNum2        pulumi.Float64PtrInput   `pulumi:"secretNum2"`
	SecretNum3        pulumi.Float64PtrInput   `pulumi:"secretNum3"`
	SecretString1     pulumi.StringPtrInput    `pulumi:"secretString1"`
	SecretString2     pulumi.StringPtrInput    `pulumi:"secretString2"`
	SecretString3     pulumi.StringPtrInput    `pulumi:"secretString3"`
	String1           pulumi.StringPtrInput    `pulumi:"string1"`
	String2           pulumi.StringPtrInput    `pulumi:"string2"`
	String3           pulumi.StringPtrInput    `pulumi:"string3"`
}

func (ToSecretOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ToSecretArgs)(nil)).Elem()
}

type ToSecretResultOutput struct{ *pulumi.OutputState }

func (ToSecretResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ToSecretResult)(nil)).Elem()
}

func (o ToSecretResultOutput) ToToSecretResultOutput() ToSecretResultOutput {
	return o
}

func (o ToSecretResultOutput) ToToSecretResultOutputWithContext(ctx context.Context) ToSecretResultOutput {
	return o
}

func (o ToSecretResultOutput) Bool1() pulumi.BoolOutput {
	return o.ApplyT(func(v ToSecretResult) bool { return v.Bool1 }).(pulumi.BoolOutput)
}

func (o ToSecretResultOutput) Bool2() pulumi.BoolOutput {
	return o.ApplyT(func(v ToSecretResult) bool { return v.Bool2 }).(pulumi.BoolOutput)
}

func (o ToSecretResultOutput) Bool3() pulumi.BoolOutput {
	return o.ApplyT(func(v ToSecretResult) bool { return v.Bool3 }).(pulumi.BoolOutput)
}

func (o ToSecretResultOutput) Int1() pulumi.IntOutput {
	return o.ApplyT(func(v ToSecretResult) int { return v.Int1 }).(pulumi.IntOutput)
}

func (o ToSecretResultOutput) Int2() pulumi.IntOutput {
	return o.ApplyT(func(v ToSecretResult) int { return v.Int2 }).(pulumi.IntOutput)
}

func (o ToSecretResultOutput) Int3() pulumi.IntOutput {
	return o.ApplyT(func(v ToSecretResult) int { return v.Int3 }).(pulumi.IntOutput)
}

func (o ToSecretResultOutput) ListBool1() pulumi.BoolArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []bool { return v.ListBool1 }).(pulumi.BoolArrayOutput)
}

func (o ToSecretResultOutput) ListBool2() pulumi.BoolArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []bool { return v.ListBool2 }).(pulumi.BoolArrayOutput)
}

func (o ToSecretResultOutput) ListBool3() pulumi.BoolArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []bool { return v.ListBool3 }).(pulumi.BoolArrayOutput)
}

func (o ToSecretResultOutput) ListInt1() pulumi.IntArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []int { return v.ListInt1 }).(pulumi.IntArrayOutput)
}

func (o ToSecretResultOutput) ListInt2() pulumi.IntArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []int { return v.ListInt2 }).(pulumi.IntArrayOutput)
}

func (o ToSecretResultOutput) ListInt3() pulumi.IntArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []int { return v.ListInt3 }).(pulumi.IntArrayOutput)
}

func (o ToSecretResultOutput) ListNum1() pulumi.Float64ArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []float64 { return v.ListNum1 }).(pulumi.Float64ArrayOutput)
}

func (o ToSecretResultOutput) ListNum2() pulumi.Float64ArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []float64 { return v.ListNum2 }).(pulumi.Float64ArrayOutput)
}

func (o ToSecretResultOutput) ListNum3() pulumi.Float64ArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []float64 { return v.ListNum3 }).(pulumi.Float64ArrayOutput)
}

func (o ToSecretResultOutput) ListSecretBool1() pulumi.BoolArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []bool { return v.ListSecretBool1 }).(pulumi.BoolArrayOutput)
}

func (o ToSecretResultOutput) ListSecretBool2() pulumi.BoolArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []bool { return v.ListSecretBool2 }).(pulumi.BoolArrayOutput)
}

func (o ToSecretResultOutput) ListSecretBool3() pulumi.BoolArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []bool { return v.ListSecretBool3 }).(pulumi.BoolArrayOutput)
}

func (o ToSecretResultOutput) ListSecretInt1() pulumi.IntArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []int { return v.ListSecretInt1 }).(pulumi.IntArrayOutput)
}

func (o ToSecretResultOutput) ListSecretInt2() pulumi.IntArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []int { return v.ListSecretInt2 }).(pulumi.IntArrayOutput)
}

func (o ToSecretResultOutput) ListSecretInt3() pulumi.IntArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []int { return v.ListSecretInt3 }).(pulumi.IntArrayOutput)
}

func (o ToSecretResultOutput) ListSecretNum1() pulumi.Float64ArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []float64 { return v.ListSecretNum1 }).(pulumi.Float64ArrayOutput)
}

func (o ToSecretResultOutput) ListSecretNum2() pulumi.Float64ArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []float64 { return v.ListSecretNum2 }).(pulumi.Float64ArrayOutput)
}

func (o ToSecretResultOutput) ListSecretNum3() pulumi.Float64ArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []float64 { return v.ListSecretNum3 }).(pulumi.Float64ArrayOutput)
}

func (o ToSecretResultOutput) ListSecretString1() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []string { return v.ListSecretString1 }).(pulumi.StringArrayOutput)
}

func (o ToSecretResultOutput) ListSecretString2() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []string { return v.ListSecretString2 }).(pulumi.StringArrayOutput)
}

func (o ToSecretResultOutput) ListSecretString3() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []string { return v.ListSecretString3 }).(pulumi.StringArrayOutput)
}

func (o ToSecretResultOutput) ListString1() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []string { return v.ListString1 }).(pulumi.StringArrayOutput)
}

func (o ToSecretResultOutput) ListString2() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []string { return v.ListString2 }).(pulumi.StringArrayOutput)
}

func (o ToSecretResultOutput) ListString3() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ToSecretResult) []string { return v.ListString3 }).(pulumi.StringArrayOutput)
}

func (o ToSecretResultOutput) MapBool1() pulumi.BoolMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]bool { return v.MapBool1 }).(pulumi.BoolMapOutput)
}

func (o ToSecretResultOutput) MapBool2() pulumi.BoolMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]bool { return v.MapBool2 }).(pulumi.BoolMapOutput)
}

func (o ToSecretResultOutput) MapBool3() pulumi.BoolMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]bool { return v.MapBool3 }).(pulumi.BoolMapOutput)
}

func (o ToSecretResultOutput) MapInt1() pulumi.IntMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]int { return v.MapInt1 }).(pulumi.IntMapOutput)
}

func (o ToSecretResultOutput) MapInt2() pulumi.IntMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]int { return v.MapInt2 }).(pulumi.IntMapOutput)
}

func (o ToSecretResultOutput) MapInt3() pulumi.IntMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]int { return v.MapInt3 }).(pulumi.IntMapOutput)
}

func (o ToSecretResultOutput) MapNum1() pulumi.Float64MapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]float64 { return v.MapNum1 }).(pulumi.Float64MapOutput)
}

func (o ToSecretResultOutput) MapNum2() pulumi.Float64MapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]float64 { return v.MapNum2 }).(pulumi.Float64MapOutput)
}

func (o ToSecretResultOutput) MapNum3() pulumi.Float64MapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]float64 { return v.MapNum3 }).(pulumi.Float64MapOutput)
}

func (o ToSecretResultOutput) MapSecretBool1() pulumi.BoolMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]bool { return v.MapSecretBool1 }).(pulumi.BoolMapOutput)
}

func (o ToSecretResultOutput) MapSecretBool2() pulumi.BoolMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]bool { return v.MapSecretBool2 }).(pulumi.BoolMapOutput)
}

func (o ToSecretResultOutput) MapSecretBool3() pulumi.BoolMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]bool { return v.MapSecretBool3 }).(pulumi.BoolMapOutput)
}

func (o ToSecretResultOutput) MapSecretInt1() pulumi.IntMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]int { return v.MapSecretInt1 }).(pulumi.IntMapOutput)
}

func (o ToSecretResultOutput) MapSecretInt2() pulumi.IntMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]int { return v.MapSecretInt2 }).(pulumi.IntMapOutput)
}

func (o ToSecretResultOutput) MapSecretInt3() pulumi.IntMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]int { return v.MapSecretInt3 }).(pulumi.IntMapOutput)
}

func (o ToSecretResultOutput) MapSecretNum1() pulumi.Float64MapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]float64 { return v.MapSecretNum1 }).(pulumi.Float64MapOutput)
}

func (o ToSecretResultOutput) MapSecretNum2() pulumi.Float64MapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]float64 { return v.MapSecretNum2 }).(pulumi.Float64MapOutput)
}

func (o ToSecretResultOutput) MapSecretNum3() pulumi.Float64MapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]float64 { return v.MapSecretNum3 }).(pulumi.Float64MapOutput)
}

func (o ToSecretResultOutput) MapSecretString1() pulumi.StringMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]string { return v.MapSecretString1 }).(pulumi.StringMapOutput)
}

func (o ToSecretResultOutput) MapSecretString2() pulumi.StringMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]string { return v.MapSecretString2 }).(pulumi.StringMapOutput)
}

func (o ToSecretResultOutput) MapSecretString3() pulumi.StringMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]string { return v.MapSecretString3 }).(pulumi.StringMapOutput)
}

func (o ToSecretResultOutput) MapString1() pulumi.StringMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]string { return v.MapString1 }).(pulumi.StringMapOutput)
}

func (o ToSecretResultOutput) MapString2() pulumi.StringMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]string { return v.MapString2 }).(pulumi.StringMapOutput)
}

func (o ToSecretResultOutput) MapString3() pulumi.StringMapOutput {
	return o.ApplyT(func(v ToSecretResult) map[string]string { return v.MapString3 }).(pulumi.StringMapOutput)
}

func (o ToSecretResultOutput) Num1() pulumi.Float64Output {
	return o.ApplyT(func(v ToSecretResult) float64 { return v.Num1 }).(pulumi.Float64Output)
}

func (o ToSecretResultOutput) Num2() pulumi.Float64Output {
	return o.ApplyT(func(v ToSecretResult) float64 { return v.Num2 }).(pulumi.Float64Output)
}

func (o ToSecretResultOutput) Num3() pulumi.Float64Output {
	return o.ApplyT(func(v ToSecretResult) float64 { return v.Num3 }).(pulumi.Float64Output)
}

func (o ToSecretResultOutput) ObjBool1() Tbool1Output {
	return o.ApplyT(func(v ToSecretResult) Tbool1 { return v.ObjBool1 }).(Tbool1Output)
}

func (o ToSecretResultOutput) ObjBool2() Tbool2Output {
	return o.ApplyT(func(v ToSecretResult) Tbool2 { return v.ObjBool2 }).(Tbool2Output)
}

func (o ToSecretResultOutput) ObjBool3() Tbool3Output {
	return o.ApplyT(func(v ToSecretResult) Tbool3 { return v.ObjBool3 }).(Tbool3Output)
}

func (o ToSecretResultOutput) ObjInt1() Tint1Output {
	return o.ApplyT(func(v ToSecretResult) Tint1 { return v.ObjInt1 }).(Tint1Output)
}

func (o ToSecretResultOutput) ObjInt2() Tint2Output {
	return o.ApplyT(func(v ToSecretResult) Tint2 { return v.ObjInt2 }).(Tint2Output)
}

func (o ToSecretResultOutput) ObjInt3() Tint3Output {
	return o.ApplyT(func(v ToSecretResult) Tint3 { return v.ObjInt3 }).(Tint3Output)
}

func (o ToSecretResultOutput) ObjNum1() Tnum1Output {
	return o.ApplyT(func(v ToSecretResult) Tnum1 { return v.ObjNum1 }).(Tnum1Output)
}

func (o ToSecretResultOutput) ObjNum2() Tnum2Output {
	return o.ApplyT(func(v ToSecretResult) Tnum2 { return v.ObjNum2 }).(Tnum2Output)
}

func (o ToSecretResultOutput) ObjNum3() Tnum3Output {
	return o.ApplyT(func(v ToSecretResult) Tnum3 { return v.ObjNum3 }).(Tnum3Output)
}

func (o ToSecretResultOutput) ObjSecretBool1() TsecretBool1Output {
	return o.ApplyT(func(v ToSecretResult) TsecretBool1 { return v.ObjSecretBool1 }).(TsecretBool1Output)
}

func (o ToSecretResultOutput) ObjSecretBool2() TsecretBool2Output {
	return o.ApplyT(func(v ToSecretResult) TsecretBool2 { return v.ObjSecretBool2 }).(TsecretBool2Output)
}

func (o ToSecretResultOutput) ObjSecretBool3() TsecretBool3Output {
	return o.ApplyT(func(v ToSecretResult) TsecretBool3 { return v.ObjSecretBool3 }).(TsecretBool3Output)
}

func (o ToSecretResultOutput) ObjSecretInt1() TsecretInt1Output {
	return o.ApplyT(func(v ToSecretResult) TsecretInt1 { return v.ObjSecretInt1 }).(TsecretInt1Output)
}

func (o ToSecretResultOutput) ObjSecretInt2() TsecretInt2Output {
	return o.ApplyT(func(v ToSecretResult) TsecretInt2 { return v.ObjSecretInt2 }).(TsecretInt2Output)
}

func (o ToSecretResultOutput) ObjSecretInt3() TsecretInt3Output {
	return o.ApplyT(func(v ToSecretResult) TsecretInt3 { return v.ObjSecretInt3 }).(TsecretInt3Output)
}

func (o ToSecretResultOutput) ObjSecretNum1() TsecretNum1Output {
	return o.ApplyT(func(v ToSecretResult) TsecretNum1 { return v.ObjSecretNum1 }).(TsecretNum1Output)
}

func (o ToSecretResultOutput) ObjSecretNum2() TsecretNum2Output {
	return o.ApplyT(func(v ToSecretResult) TsecretNum2 { return v.ObjSecretNum2 }).(TsecretNum2Output)
}

func (o ToSecretResultOutput) ObjSecretNum3() TsecretNum3Output {
	return o.ApplyT(func(v ToSecretResult) TsecretNum3 { return v.ObjSecretNum3 }).(TsecretNum3Output)
}

func (o ToSecretResultOutput) ObjSecretString1() TsecretString1Output {
	return o.ApplyT(func(v ToSecretResult) TsecretString1 { return v.ObjSecretString1 }).(TsecretString1Output)
}

func (o ToSecretResultOutput) ObjSecretString2() TsecretString2Output {
	return o.ApplyT(func(v ToSecretResult) TsecretString2 { return v.ObjSecretString2 }).(TsecretString2Output)
}

func (o ToSecretResultOutput) ObjSecretString3() TsecretString3Output {
	return o.ApplyT(func(v ToSecretResult) TsecretString3 { return v.ObjSecretString3 }).(TsecretString3Output)
}

func (o ToSecretResultOutput) ObjString1() Tstring1Output {
	return o.ApplyT(func(v ToSecretResult) Tstring1 { return v.ObjString1 }).(Tstring1Output)
}

func (o ToSecretResultOutput) ObjString2() Tstring2Output {
	return o.ApplyT(func(v ToSecretResult) Tstring2 { return v.ObjString2 }).(Tstring2Output)
}

func (o ToSecretResultOutput) ObjString3() Tstring3Output {
	return o.ApplyT(func(v ToSecretResult) Tstring3 { return v.ObjString3 }).(Tstring3Output)
}

func (o ToSecretResultOutput) SecretBool1() pulumi.BoolOutput {
	return o.ApplyT(func(v ToSecretResult) bool { return v.SecretBool1 }).(pulumi.BoolOutput)
}

func (o ToSecretResultOutput) SecretBool2() pulumi.BoolOutput {
	return o.ApplyT(func(v ToSecretResult) bool { return v.SecretBool2 }).(pulumi.BoolOutput)
}

func (o ToSecretResultOutput) SecretBool3() pulumi.BoolOutput {
	return o.ApplyT(func(v ToSecretResult) bool { return v.SecretBool3 }).(pulumi.BoolOutput)
}

func (o ToSecretResultOutput) SecretInt1() pulumi.IntOutput {
	return o.ApplyT(func(v ToSecretResult) int { return v.SecretInt1 }).(pulumi.IntOutput)
}

func (o ToSecretResultOutput) SecretInt2() pulumi.IntOutput {
	return o.ApplyT(func(v ToSecretResult) int { return v.SecretInt2 }).(pulumi.IntOutput)
}

func (o ToSecretResultOutput) SecretInt3() pulumi.IntOutput {
	return o.ApplyT(func(v ToSecretResult) int { return v.SecretInt3 }).(pulumi.IntOutput)
}

func (o ToSecretResultOutput) SecretNum1() pulumi.Float64Output {
	return o.ApplyT(func(v ToSecretResult) float64 { return v.SecretNum1 }).(pulumi.Float64Output)
}

func (o ToSecretResultOutput) SecretNum2() pulumi.Float64Output {
	return o.ApplyT(func(v ToSecretResult) float64 { return v.SecretNum2 }).(pulumi.Float64Output)
}

func (o ToSecretResultOutput) SecretNum3() pulumi.Float64Output {
	return o.ApplyT(func(v ToSecretResult) float64 { return v.SecretNum3 }).(pulumi.Float64Output)
}

func (o ToSecretResultOutput) SecretString1() pulumi.StringOutput {
	return o.ApplyT(func(v ToSecretResult) string { return v.SecretString1 }).(pulumi.StringOutput)
}

func (o ToSecretResultOutput) SecretString2() pulumi.StringOutput {
	return o.ApplyT(func(v ToSecretResult) string { return v.SecretString2 }).(pulumi.StringOutput)
}

func (o ToSecretResultOutput) SecretString3() pulumi.StringOutput {
	return o.ApplyT(func(v ToSecretResult) string { return v.SecretString3 }).(pulumi.StringOutput)
}

func (o ToSecretResultOutput) String1() pulumi.StringOutput {
	return o.ApplyT(func(v ToSecretResult) string { return v.String1 }).(pulumi.StringOutput)
}

func (o ToSecretResultOutput) String2() pulumi.StringOutput {
	return o.ApplyT(func(v ToSecretResult) string { return v.String2 }).(pulumi.StringOutput)
}

func (o ToSecretResultOutput) String3() pulumi.StringOutput {
	return o.ApplyT(func(v ToSecretResult) string { return v.String3 }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(ToSecretResultOutput{})
}
