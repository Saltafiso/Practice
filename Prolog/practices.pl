% 1
pairFlip([], []).
pairFlip([X|[]], [Y|[]]) :-
  X = Y.
pairFlip([X1,X2|Xs], [Y1,Y2|Ys]) :-
  X1 = Y2,
  Y1 = X2,
  pairFlip(Xs,Ys).
% 2    
help([],[]).
help([X|Xs], [X|Ys]) :-
  help(Xs,Ys).
help([_|Xs], Ys) :-
  help(Xs,Ys).

sublistSum(Lst, V, Sub) :-
  help(Lst,Sub),
  sum_list(Sub,V).
% 3
legalCourse([]).
legalCourse([(N1+N2+_)|Xs]) :-
  not(N1 = N2),
  Tmp1 = (N1+N2+_),
  not(member(Tmp1,Xs)),
  Tmp2 = (N2+N1+_),
  not(member(Tmp2,Xs)),
  legalCourse(Xs).
% 4
studentCount(_,[],0).
studentCount(N,[(N1+N2+_)|Xs],V) :-
  (N = N1;N = N2),
  studentCount(N,Xs,V1),
  V is V1+1.
studentCount(N,[(N1+N2+_)|Xs], V) :-
  not(N = N1;N = N2),
  studentCount(N,Xs,V).
% 5
partners(_,[],[]).
partners(N1,[(N1+N2+_)|Xs], Lst) :-
  partners(N1,Xs,Lst1),
  Lst = [N2|Lst1].
partners(N2,[(N1+N2+_)|Xs], Lst) :-
  partners(N2,Xs,Lst1),
  Lst = [N1|Lst1].
partners(N,[(N1+N2+_)|Xs], Lst) :-
  not(N = N1;N = N2),
  partners(N,Xs,Lst).
% 6
courseAvg([],0).
courseAvg(Lst,V) :- 
  length(Lst,Len),
  h_courseAvg(Lst,Sum),
  V is Sum / Len.
h_courseAvg([],0).
h_courseAvg([(_+_+M)|Xs],A) :-
  h_courseAvg(Xs,A1),
  A is A1 +M.
% 7
studentAvg(_,[],0).
studentAvg(N,Lst,V) :- 
  h_studentAvg(N,Lst,Sum,L),
  V is Sum / L.
h_studentAvg(_,[],0,0).
h_studentAvg(N,[(N1+N2+M)|Xs],A,L) :-
  (N = N1;N = N2),
  h_studentAvg(N,Xs,A1,L1),
  L is L1 +1,
  A is A1 +M.
h_studentAvg(N,[(N1+N2+_)|Xs],A,L) :-
  not(N = N1;N = N2),
  h_studentAvg(N,Xs,A,L).
% 8
students([],[]).
students([(N1+N2+_)|Xs],Ys) :-
  students(Xs,Ys1),
  not(member(N2,Ys1)),
  T = [N2|Ys1],
  not(member(N1,T)),
  Ys = [N1|T].
students([(N1+N2+_)|Xs],Ys) :-
  students(Xs,Ys1),
  not(member(N2,Ys1)),
  T = [N2|Ys1],
  member(N1,T),
  Ys = T.
students([(N1+N2+_)|Xs],Ys) :-
  students(Xs,Ys1),
  member(N2,Ys1),
  T = Ys1,
  not(member(N1,T)),
  Ys = [N1|T].
students([(N1+N2+_)|Xs],Ys) :-
  students(Xs,Ys1),
  member(N2,Ys1),
  T = Ys1,
  member(N1,T),
  Ys = T.
