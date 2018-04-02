// Input .geo for quad domain 
// author: Juan Gomez 
 
c =   0.100  ; 		// for size elements 
 
l=   5.000 ; 
h=   5.000 ; 
 
// Define vertex points 
 
Point(1) = {-h/2 , 0 , 0, c};		// {x,y,z, size} 
Point(2) = {h/2  , 0 , 0, c}; 
Point(3) = {h/2  , l , 0, c}; 
Point(4) = {-h/2 , l , 0, c}; 
 
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
