% clear the screen and the workspace
clc

%% set the parameters
% set the sampling time
Ts = 0.1;

%% simulation
% create a plant model
G = tf(1, [1 2 10]);
% create a mpc controller
mpc = mpc(G, Ts);
% set the prediction horizon
mpc.PredictionHorizon = 5;
% set the control horizon
mpc.ControlHorizon = 5;
% set the weights
mpc.Weights.MV = 1;
mpc.Weights.MVRate = 0.1;
mpc.Weights.OV = 1;
mpc.Weights.ECR = 1;
% set the initial state
x0 = 0;
% set the reference
r = 1;
% set the simulation time
T = 10;
% create a simulation model
sim = mpcsim(mpc, T);
% set the initial state
sim.InitialCondition = x0;
% set the reference
sim.Ref = r;
% run the simulation
sim.run;
