/* common screw parameter
length
pitch = length/rotations: the distance between the turns of the thread
outside_diameter
inner_diameter: thickness of the shaft
*/

module helix(pitch, length){

}

module auger(pitch, length, outside_diameter, inner_diameter) {
    rotations = length/pitch;
	union() {
		linear_extrude(height=length, center=false, convexity=10, twist=360*rotations, slices=100, $fn=1000)
			polygon(points=[[10,10],[100,1],[100,-1],[10,-10]], paths=[[0,1,2,3]]);
		cylinder(h=length, r=20);
	}
}

translate([300, 0, 0]) auger(100, 300);


module ball_groove(pitch, rotations, diameter, bearing_radius=10) {
    rotations = length/pitch;
    linear_extrude(height = 10, center = false, convexity = 10, twist = 360, $fn = 1000)
        translate([diameter, 0, 0])
        circle(r = bearing_radius);
}

ball_groove(100, 300, 10);

module ball_screw(pitch, length, bearing_radius=2) {

}
