// Input .geo for quad domain 
// author: Juan Gomez 
 
c =   0.125  ; 		// for size elements 
 
l=   0.500 ; 
h=   1.000 ; 
 
// Define vertex points 
 
Point(1) = {0 , 0 , 0, c};		// {x,y,z, size} 
Point(2) = {h  , 0 , 0, c}; 
Point(3) = {h  , l , 0, c}; 
 Point(4) = {0 , l , 0, c}; 
 
// Define boundary lines 
Line(1) = {1, 2};		// {Initial_point, end_point} 
Line(2) = {2, 3}; 
Line(3) = {3, 4}; 
Line(4) = {4, 1}; 
 
// Joint Lines 
   Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... } 
 
// surface for mesh 			// {Id_Loop} 
Plane Surface(1) = {1}; 
 
// For Mesh 4 nodes 
Recombine Surface {1};			// {Id_Surface} 
 
// "Structure" mesh 
Transfinite Surface {1};		// {Id_Surface} 
 
Physical Surface(100) = {1}; 
