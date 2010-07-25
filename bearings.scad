// License: GPL 2.0

//Todo: placeholder; should generate standard + cusom bearing mounting holes
module bearing_hole(outer_radius, hole=true, mochup=true)
{
	union()
	{
		if (mochup==true) %translate([0,0,-1.5])cylinder(r=outer_radius,h=3);
		if (hole==true) circle(r=outer_radius);
	}
}
