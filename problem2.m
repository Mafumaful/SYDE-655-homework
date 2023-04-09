% clear the screen and the workspace
clc

%% set the parameters
% set the sampling time
Ts = 0.1;
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
model.y.penalty = QuadFunction(diag(1));
model.u.with('deltaMin');
model.u.with('deltaMax');
model.u.deltaMin = -1;
model.u.deltaMax = 1;
model.u.min = -10;
model.u.max = 10;

% set reference, in the first 5 seconds, the reference is 1, then it is 0
yref = [ones(1, 5 / Ts), zeros(1, 5 / Ts)];
model.y.with('reference');
model.y.reference = 'free';

ctrl = MPCController(model, 6);
loop = ClosedLoop(ctrl, model);
x0 = [0; 0];
u0 = 0;

data = loop.simulate(x0, Nsim, 'u.previous', u0, 'y.reference', yref);

subplot(2, 1, 1); hold on;
%% plot the results
% legend('y', 'yref')
plot(1:Nsim, data.Y(1:Nsim), 'linewidth', 2);
stairs(1:Nsim, yref, 'r--', 'linewidth', 2);
axis([1, Nsim, -0.5, 1.5]);
title('state')
%% plot the input
subplot(2, 1, 2); hold on;
stairs(1:Nsim, data.U, 'linewidth', 2);
axis([1, Nsim, -1, 12]);
title('input')
