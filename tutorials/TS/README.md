> [!IMPORTANT]  
> This tutorial is a Work-In-Progress, and is entirely from personal experience, which will differ system to system. So it must be used as advice and not trusted entirely! So feel free to add to this tutorial, as well as to question points within it.

# Introduction
This tutorial aims to provide more guidance for the **tedious** process of finding Transition States. Should you need any further help, included are some resources which provide general information on finding *pesky* Transition States.

Lastly, softwares, techniques, and methodologies are constantly improving, so should any section of this tutorial become outdated, **please** update it. If you can't, **please** at least place it in the [To-Do](../../README.md) section on the front page!

# Index
- [Gaussian](#gaussian)
- [Orca](#orca)

# Gaussian 
### Tutorials
[The art of finding transition structures](https://thisisntnathan.github.io/dftCourse/LongCourse/transitionStructureSearch.html#verification)

[The 'art' of finding Transition States](https://joaquinbarroso.com/2016/05/26/the-art-of-finding-transition-states-part-1/)

### Workflow


```mermaid
flowchart TD
    A[Looking for a TS using Gaussian] ---> B[Do you know which bonds?]
    B -- Yes --> C{Scan}
    C -- Failed --> D[TBD]
    C -- Normal Termination --> E[Is the curve Quadratic?]
    E -- No --> F[Try a different range]
    F --> E
    E -- Yes --> G{TS Search at 
        3 highest
        energies}
    G -- Failed --> H(Retry with Maxstep=5)
    H --> G
    G -- Normal Termination --> I[Extra Imaginary Frequencies?]
    I -- No --> J[Correct Vibrational Mode?]
    J -- Yes --> K(Done!)
    J -- No --> L[Below -10 cm-1?]
    L -- Yes --> K
    L -- No --> M{Manually displace
        extra negative
        frequencies}
    M --> I
    I -- Yes --> N(Done!)

```

# Orca
### Tutorials
[Vibrational Frequencies](https://www.faccts.de/docs/orca/5.0/tutorials/prop/freq.html)

[NEB-TS](https://www.faccts.de/docs/orca/5.0/tutorials/react/nebts.html)

### Workflow



