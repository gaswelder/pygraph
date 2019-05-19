## Clifford Attractors

Attributed to Clifford Pickover.

Definition

    x[n+1] = sin(a * y[n]) + c * cos(a * x[n])
    y[n+1] = sin(b * x[n]) + d * cos(b * y[n])

where a, b, c, d are variabies that define each attractor.
Examples:

    a = 1.6, b = -0.6, c = -1.2, d = 1.6
    a = 1.7, b = 1.7, c = 0.06, d = 1.2
    a = 1.3, b = 1.7, c = 0.5, d = 1.4
    a = 1.5, b = -1.8, c = 1.6, d = 0.9
    a = -1.4, b = 1.6, c = 1.0, d = 0.7
    a = 1.1, b = -1.0, c = 1.0, d = 1.5

Set up a grid of pixel values.
Evaluate points on the attractor and just increment each cell of the grid if the attractor passes through it.
So it's essentially a 2D histogram for occupancy.

As this is a "chaotic" process, the image will be noisy unless enough "exposure" is achieved by looping many enough times.
You'd stop the loop when the image is nice and smooth enough, but how do you detect that?

One option is to just specify a huge number that will certainly be enough.

Another is to stop iterating when you land on a pixel with a value above some preset.
But in this case you can start too early if the attractor has high dynamic range
(meaning, a point may reach saturation well before all other points were even touched).

Coloring is another problem.
One way is to just apply colors based on the resulting darkness of pixels.
This is "just" a density mapping of the histogram and allow for colouring based upon other attributes of the attractor path, such as curvature.
But such attributes can be encoded into the histogram encoding, for example the amount added to a cell being a function of curvature.
