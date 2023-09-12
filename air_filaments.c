#include "axi.h"
#include "navier-stokes/centered.h"
//#define mu(f)  (1./(clamp(f,0,1)*(1./mu1 - 1./mu2) + 1./mu2))
#include "two-phase.h"
#include "tension.h"
#include "navier-stokes/conserving.h"
//#define L_domain 50.0
//#include "view.h"
#define aspect_ratio 12
#define length (aspect_ratio*gas_thickness)
#define Circle sq(x-(0.5-length/2))+sq(y)-sq(radius) 
#define gas_thickness 0.02
#define radius (gas_thickness/2.)
#define Oh 1.0
#define sur_tens 1.53
#define gas_dens 0.0012
#define liq_dens 1.0
#define mu_liq (Oh*sqrt(sur_tens*gas_thickness*liq_dens))
#define Max_Level 11   
#define FILTRED

//define the configuration of the filament, aspect ratio 
double geometry(double x, double y)
{
    double Line_up = (gas_thickness/2) - y;
    double Line_right = (0.5+length/2)-x;
    double retrangle = min(Line_right,Line_up); 
    double circle = sq(radius) - sq(x-(0.5+length/2)) - sq(y);
    double shape_final = max(retrangle,circle);
   return -shape_final;
} 
int main()
{
   // size(L_domain);
    origin(0.,0.);
    init_grid(1<<8);
    rho1 =  liq_dens; //properties for gas and liquid
    rho2 = gas_dens;
    mu1 = mu_liq;
    mu2 = mu1/58.8;
    f.sigma = sur_tens;
    run();
}

event init(i=0)
{   if (!restore (file = "restart")) {
    refine(x<(0.5+(length/2)) && x>(0.5-(length/2)) && y<0.02 && y>0.0 && level < Max_Level);
    refine(x>((0.5+(length/2))) && sq(y)+sq(x-((0.5+(length/2))))>sq(0.) && sq(y)+sq(x-(0.5+(length/2)))<sq(gas_thickness) && level < Max_Level);
    refine(x<((0.5-length/2)) && sq(y)+sq(x-((0.5+(length/2))))>sq(0.) && sq(y)+sq(x-(0.5-(length/2)))<sq(gas_thickness) && level < Max_Level);
    fraction(f, x<=0.5-length/2 ? Circle : geometry(x,y));
    }

}

event logfile (i++) {
  if (i == 0)
    fprintf (stderr,
             "t dt mgp.i mgpf.i mgu.i grid->tn perf.t perf.speed\n");
  fprintf (stderr, "%g %g %d %d %d %ld %g %g\n", 
           t, dt, mgp.i, mgpf.i, mgu.i,
           grid->tn, perf.t, perf.speed);
} 
/*
event movie (t += 1e-3)
{
view (quat = {0.000, 0.000, 0.000, 0.500},
      fov = 7, 
      tx = -0.500, ty = 0.00, 
      width = 1146, height = 840);
squares (color = "u.x", min = -1, max = 1, spread = -1, linear = true);
draw_vof (c = "f");
vectors ();

  scalar omega[];
  vorticity (u, omega);
  view (tx = -0.5);
  clear();
  draw_vof ("f");
  squares ("omega", linear = true, spread = 10);
  box ();
  save ("movie1.mp4");
}
*/
event snapshot (t = 0.1; t += 0.1; t <= 10) {
  char name[80];
  sprintf (name, "snapshot-%g", t);
  scalar pid[];
  foreach()
    pid[] = fmod(pid()*(npe() + 37), npe());
  boundary ({pid});
  dump (name);
}

event snap (t = 0.;t += 1e-3 ; t <= 10) {
  char name[80];
  sprintf (name, "snapshot-%3.3f.gfs", t);
  scalar omega[];
  vorticity (u, omega);
 output_gfs (file = name, t = t, list = {f,u,p,omega});
 sprintf (name, "restart");
 dump (name);
}

event adapt(i++)
{
    adapt_wavelet({f,u},(double []){1e-4,1e-2,1e-2},Max_Level,5);       
}

/*
char file_name[100];
event outputfile(t+=0.001)
{
    p.nodump = false;
    sprintf(file_name,"dumpfile_%.3f",t);
    dump(file=file_name);
}

event end(t=20.)
{
    
}  

*/

