<p>
  <a href="https://github.com/JuliaSmoothOptimizers"><img width="150" align='left' src="https://raw.githubusercontent.com/tmigot/tmigot/main/logo-jso.png"></a>
</p>

# Welcome to JuliaSmoothOptimizers (JSO)

JSO is an organization dedicated to numerical linear algebra and optimization, containing packages to model, solve, benchmark and analyze results efficiently.
We aim, among other things, to provide cutting-edge and original solvers and tools for researchers.

Feel free to visit our website [juliasmoothoptimizers.github.io](https://juliasmoothoptimizers.github.io) for recent updates on the organization.

Interested in the organization? Have a look at [@dpo's presentation of JSO on Youtube](https://www.youtube.com/watch?v=p5Z5QGOUZhE) 📽️ at the JuliaCon2022.

## Want to contribute?

New contributors are always welcome 👋! 

First-time contributors might want to have a look at available issues with [the label `good first issue`](https://github.com/search?q=user%3AJuliaSmoothOptimizers+label%3A"good+first+issue"+language%3AJulia+state%3Aopen&type=Issues&ref=advsearch&l=Julia&l=).
Please visit [Contributing section of the website](https://juliasmoothoptimizers.github.io/contributing/) for guidelines.
One of our simplest packages for new contributors is [OptimizationProblems.jl](https://juliasmoothoptimizers.github.io/OptimizationProblems.jl/dev/contributing/).

## Looking for tutorials?

🥋: All packages have their own documentation. You can also access the [tutorial section of the JSO website](https://juliasmoothoptimizers.github.io/tutorials/)

🎬: Follow [@abelsiqueira's youtube channel](https://www.youtube.com/playlist?list=PLOOY0eChA1uxmm8G2caFpdX7X9NjgpDUY) for more tutorials in videos!

Feel free to open [a discussion](https://github.com/orgs/JuliaSmoothOptimizers/discussions) if you can't find answers to your questions.

## Looking for a package?

JuliaSmoothOptimizers contains several packages for modeling and solving linear algebra and optimization problems.
The optimization solvers all rely on a unified API to communicate with the models, which is the [NLPModels API](https://github.com/JuliaSmoothOptimizers/NLPModels.jl).

You might also be interested in [SolverBenchmark.jl](https://github.com/JuliaSmoothOptimizers/SolverBenchmark.jl) to easily compare your solver via performance profiles or tables available in LaTeX or markdown format!

### Linear algebra (incl. linear least squares)

- Efficiently model linear problems 🤠: [LinearOperators.jl](https://github.com/JuliaSmoothOptimizers/LinearOperators.jl), [SparseMatricesCOO.jl](https://github.com/JuliaSmoothOptimizers/SparseMatricesCOO.jl), [LLSModels.jl](https://github.com/JuliaSmoothOptimizers/LLSModels.jl)
- Solve linear problems with iterative methods 🥳: [Krylov.jl](https://github.com/JuliaSmoothOptimizers/Krylov.jl) 
- Computing a sparse factorization 👾: [LDLFactorizations.jl](https://github.com/JuliaSmoothOptimizers/LDLFactorizations.jl), [HSL.jl](https://github.com/JuliaSmoothOptimizers/HSL.jl), [MUMPS.jl](https://github.com/JuliaSmoothOptimizers/MUMPS.jl), [QRMumps.jl](https://github.com/JuliaSmoothOptimizers/QRMumps.jl)
- Construct a preconditionner 🚀: [BasicLU.jl](https://github.com/JuliaSmoothOptimizers/BasicLU.jl), [LimitedLDLFactorizations.jl](https://github.com/JuliaSmoothOptimizers/LimitedLDLFactorizations.jl), [AMD.jl](https://github.com/JuliaSmoothOptimizers/AMD.jl)
- Access test systems 🤼: [SuiteSparseMatrixCollection.jl](https://github.com/JuliaSmoothOptimizers/SuiteSparseMatrixCollection.jl)

### Linear and quadratic optimization problems

- Model a problem with quadratic objective and linear constraints 🦸: [QuadraticModels.jl](https://github.com/JuliaSmoothOptimizers/QuadraticModels.jl), [QPSReader.jl](https://github.com/JuliaSmoothOptimizers/QPSReader.jl)
- Solve linear and quadratic models 🎅: [RipQP.jl](https://github.com/JuliaSmoothOptimizers/RipQP.jl), [QuadraticModelsCPLEX.jl](https://github.com/JuliaSmoothOptimizers/QuadraticModelsCPLEX.jl), [QuadraticModelsXpress.jl](https://github.com/JuliaSmoothOptimizers/QuadraticModelsXpress.jl), [QuadraticModelsGurobi.jl](https://github.com/JuliaSmoothOptimizers/QuadraticModelsGurobi.jl)

### Nonlinear Least squares

- Model nonlinear least-squares problems 🧙: [ADNLPModels.jl](https://github.com/JuliaSmoothOptimizers/ADNLPModels.jl), [NLPModelsJuMP](https://github.com/JuliaSmoothOptimizers/NLPModelsJuMP.jl) 
- Solve nonlinear least squares 🧐: [CaNNOLeS.jl](https://github.com/JuliaSmoothOptimizers/CaNNOLeS.jl), [JSOSolvers](https://github.com/JuliaSmoothOptimizers/JSOSolvers.jl)
- Access test problems 🤺: [BundleAdjustmentModels.jl](https://github.com/JuliaSmoothOptimizers/BundleAdjustmentModels.jl), [NLSProblems.jl](https://github.com/JuliaSmoothOptimizers/NLSProblems.jl), [OptimizationProblems.jl](https://github.com/JuliaSmoothOptimizers/OptimizationProblems.jl)

### General nonlinear optimization

- Model general optimization problems 💪: [ADNLPModels.jl](https://github.com/JuliaSmoothOptimizers/ADNLPModels.jl), [KnetNLPModels.jl](https://github.com/JuliaSmoothOptimizers/KnetNLPModels.jl), [PDENLPModels.jl](https://github.com/JuliaSmoothOptimizers/PDENLPModels.jl)
- Load models from other modeling systems 🦅: [NLPModelsJuMP](https://github.com/JuliaSmoothOptimizers/NLPModelsJuMP.jl), [AmplNLReader.jl](https://github.com/JuliaSmoothOptimizers/AmplNLReader.jl), [CUTEst.jl](https://github.com/JuliaSmoothOptimizers/CUTEst.jl)
- Solve unconstrained and bound-constrained models 👍: [JSOSolvers](https://github.com/JuliaSmoothOptimizers/JSOSolvers.jl)
- Solve general optimization problems 🤘: [DCISolver.jl](https://github.com/JuliaSmoothOptimizers/DCISolver.jl), [NLPModelsIpopt.jl](https://github.com/JuliaSmoothOptimizers/NLPModelsIpopt.jl), [NLPModelsKnitro.jl](https://github.com/JuliaSmoothOptimizers/NLPModelsKnitro.jl), [Percival.jl](https://github.com/JuliaSmoothOptimizers/Percival.jl)
- Access a collection of test problems 🤖: [CUTEst.jl](https://github.com/JuliaSmoothOptimizers/CUTEst.jl), [OptimizationProblems.jl](https://github.com/JuliaSmoothOptimizers/OptimizationProblems.jl)


#### Acknowledgements

We gratefully acknowledge the support of MacStadium for providing us with hardware use for continuous integration at JSO!

<img src="https://user-images.githubusercontent.com/38760/189140951-cebeb891-e18f-49e2-8ff8-63b2b1afd4f9.png" width="200">
