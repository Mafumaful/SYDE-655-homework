% clear the screen and the workspace
clc

%% set the parameters
% set the sampling time
Ts = 0.01;
T_total = 10;
% samples
Nsim = T_total / Ts;

%% simulation
% create a plant model
G = tf(1, [1 2 10]);
% return state-space model
[A, B, C, D] = ssdata(G);
% create the model
model = LTISystem('A', A, 'B', B, 'C', C, 'D', D, 'Ts', Ts);
model.u.penalty = QuadFunction(diag(3));
model.y.penalty = QuadFunction(diag(10));

% set reference, in the first 5 seconds, the reference is 1, then it is 0
yref = [ones(1, 5 / Ts), zeros(1, 5 / Ts)];
model.y.with('reference');
model.y.reference = 'free';

ctrl = MPCController(model, 6);
loop = ClosedLoop(ctrl, model);
x0 = [0; 0];

data = loop.simulate(x0, Nsim, 'y.reference', yref);

plot(1:Nsim, data.Y);
hold on;
