<p>
  <a href="https://github.com/JuliaSmoothOptimizers"><img width="150" align='left' src="https://raw.githubusercontent.com/tmigot/tmigot/main/logo-jso.png"></a>
</p>

# Welcome to JuliaSmoothOptimizers (JSO)

JSO is an organization dedicated to numerical linear algebra and optimization, containing packages to model, solve, benchmark and analyze results efficiently.
We aim, among other things, to provide cutting-edge and original solvers and tools for researchers.

Feel free to visit our website [juliasmoothoptimizers.github.io](https://juliasmoothoptimizers.github.io) to get recent updates of the organization.

Interested in the organization? Have a look at [@dpo's presentation of JSO on Youtube](https://www.youtube.com/watch?v=p5Z5QGOUZhE) 📽️ during the JuliaCon2022.

## Want to contribute?

New contributors are always welcome 👋! 

First-time contributors can have a look at available issues with [the label `good first issue`](https://github.com/search?q=user%3AJuliaSmoothOptimizers+label%3A"good+first+issue"+language%3AJulia+state%3Aopen&type=Issues&ref=advsearch&l=Julia&l=).
You can visit [Contributing section of the website](https://juliasmoothoptimizers.github.io/contributing/) for some of our guidelines.
One of our simplest package for new contributers is [OptimizationProblems.jl](https://juliasmoothoptimizers.github.io/OptimizationProblems.jl/dev/contributing/).

## Looking for tutorials

🥋: All the packages have their own documentation. You can also access the [tutorial section of JSO's website](https://juliasmoothoptimizers.github.io/tutorials/)

🎬: Follow [@abelsiqueira's youtube channel](https://www.youtube.com/playlist?list=PLOOY0eChA1uxmm8G2caFpdX7X9NjgpDUY) for more tutorials in videos!

Feel free to open an issue or a discussion if you can't find answers to your questions.

## Looking for a package?

JuliaSmoothOptimizers contains several packages for modeling and solving linear algebra and optimization problems.
The optimization solvers all rely on a unified API to communicate with the models, which is the [NLPModels API](https://github.com/JuliaSmoothOptimizers/NLPModels.jl).

You might also be interest in [SolverBenchmark.jl](https://github.com/JuliaSmoothOptimizers/SolverBenchmark.jl) to easily compare your solver via performance profiles or tables available in LaTeX or markdown format!

### Linear algebra

- Efficient modeling of linear systems 🤠: [LinearOperators.jl](https://github.com/JuliaSmoothOptimizers/LinearOperators.jl), [SparseMatricesCOO.jl](https://github.com/JuliaSmoothOptimizers/SparseMatricesCOO.jl), [LLSModels.jl](https://github.com/JuliaSmoothOptimizers/LLSModels.jl)
- Solving linear systems with iterative methods 🥳: [Krylov.jl](https://github.com/JuliaSmoothOptimizers/Krylov.jl) 
- Compute matrix factorization 👾: [LDLFactorizations.jl](https://github.com/JuliaSmoothOptimizers/LDLFactorizations.jl), [HSL.jl](https://github.com/JuliaSmoothOptimizers/HSL.jl), [MUMPS.jl](https://github.com/JuliaSmoothOptimizers/MUMPS.jl), [QRMumps.jl](https://github.com/JuliaSmoothOptimizers/QRMumps.jl), [AMD.jl](https://github.com/JuliaSmoothOptimizers/AMD.jl)
- Preconditionner: [BasicLU.jl](https://github.com/JuliaSmoothOptimizers/BasicLU.jl), [LimitedLDLFactorizations.jl](https://github.com/JuliaSmoothOptimizers/LimitedLDLFactorizations.jl)
- Test systems 🤼: [SuiteSparseMatrixCollection.jl](https://github.com/JuliaSmoothOptimizers/SuiteSparseMatrixCollection.jl)

### Quadratic optimization problems

- Model the problem with quadratic objective and linear constraints 🦸: [QuadraticModels.jl](https://github.com/JuliaSmoothOptimizers/QuadraticModels.jl), [QPSReader.jl](https://github.com/JuliaSmoothOptimizers/QPSReader.jl)
- Solve quadratic models 🎅: [RipQP.jl](https://github.com/JuliaSmoothOptimizers/RipQP.jl), [QuadraticModelsCPLEX.jl](https://github.com/JuliaSmoothOptimizers/QuadraticModelsCPLEX.jl), [QuadraticModelsXpress.jl](https://github.com/JuliaSmoothOptimizers/QuadraticModelsXpress.jl), [QuadraticModelsGurobi.jl](https://github.com/JuliaSmoothOptimizers/QuadraticModelsGurobi.jl)

### (Nonlinear) Least squares

- Model nonlinear least squares 🧙: [ADNLPModels.jl](https://github.com/JuliaSmoothOptimizers/ADNLPModels.jl), [NLPModelsJuMP](https://github.com/JuliaSmoothOptimizers/NLPModelsJuMP.jl) 
- Solvers specific for nonlinear least squares 🧐: [CaNNOLeS.jl](https://github.com/JuliaSmoothOptimizers/CaNNOLeS.jl), [JSOSolvers](https://github.com/JuliaSmoothOptimizers/JSOSolvers.jl)
- Test problems 🤺: [BundleAdjustmentModels.jl)](https://github.com/JuliaSmoothOptimizers/BundleAdjustmentModels.jl), [NLSProblems.jl](https://github.com/JuliaSmoothOptimizers/NLSProblems.jl), [OptimizationProblems.jl](https://github.com/JuliaSmoothOptimizers/OptimizationProblems.jl)

### Generic optimization problems 🤯

- Model general optimization problems 💪: [ADNLPModels.jl](https://github.com/JuliaSmoothOptimizers/ADNLPModels.jl), [KnetNLPModels.jl](https://github.com/JuliaSmoothOptimizers/KnetNLPModels.jl), [PDENLPModels.jl](https://github.com/JuliaSmoothOptimizers/PDENLPModels.jl)
- Load models from other modeling systems 🦅: [NLPModelsJuMP](https://github.com/JuliaSmoothOptimizers/NLPModelsJuMP.jl), [AmplNLReader.jl](https://github.com/JuliaSmoothOptimizers/AmplNLReader.jl), [CUTEst.jl](https://github.com/JuliaSmoothOptimizers/CUTEst.jl)
- Solvers for unconstrained and bound-constrained models 👍: [JSOSolvers](https://github.com/JuliaSmoothOptimizers/JSOSolvers.jl)
- Solve generic optimization problems 🤘: [DCISolver.jl](https://github.com/JuliaSmoothOptimizers/DCISolver.jl), [NLPModelsIpopt.jl](https://github.com/JuliaSmoothOptimizers/NLPModelsIpopt.jl), [NLPModelsKnitro.jl](https://github.com/JuliaSmoothOptimizers/NLPModelsKnitro.jl), [Percival.jl](https://github.com/JuliaSmoothOptimizers/Percival.jl)
- Collection of test problems 🤖: [CUTEst.jl](https://github.com/JuliaSmoothOptimizers/CUTEst.jl), [OptimizationProblems.jl](https://github.com/JuliaSmoothOptimizers/OptimizationProblems.jl)
