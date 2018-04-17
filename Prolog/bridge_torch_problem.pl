% 10176970
% Congwei Chen
moveNorth(North, South, Moves, Time) :-
  select(P1/T1, South, Res1),
  select(P2/T2, Res1, Res2),
  P1 @< P2,
  North1 = [P1/T1,P2/T2|North],
  moveSouth(North1,Res2,Moves1, Time1),
  T is max(T1,T2),
  Time is Time1 + T,
  Moves = [P1 + P2|Moves1].
moveSouth(_,[],[],0).
moveSouth(North, South, Moves, Time) :-
  select(P/T,North,Res),
  South1 = [P/T|South],
  moveNorth(Res,South1,Moves1,Time1),
  Moves = [P|Moves1],
  Time is Time1 + T.
moveFamily(Name, Max, Moves, Time) :- 
  family(Name, List),
  moveNorth([],List,Moves,Time),
  Time =< Max.
