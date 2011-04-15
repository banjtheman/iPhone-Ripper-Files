//
//  SecondView.m
//  ThreeViewNav
//
//  Created by Brendan Christopher Fruin on 4/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "ThreeViewNavAppDelegate.h"
#import "SecondView.h"
#import "ThirdView.h"

@implementation SecondView

-(IBAction)anotherViewButtonPushed:(id)sender {
	ThreeViewNavAppDelegate *appDelegate = [[UIApplication sharedApplication] delegate];
	ThirdView *thirdViewController = [[ThirdView alloc] initWithNibName:nil bundle:nil];
	[appDelegate.navigationController pushViewController:thirdViewController animated:NO];
	
	[thirdViewController release];
	
}

-(IBAction)anotherButtonPushed:(id)sender {	
	if (!buttonCreated) {
		UIButton *buttonToAdd = [UIButton buttonWithType:UIButtonTypeRoundedRect];
		[buttonToAdd addTarget:self action:@selector(dynamicButtonAction)
			  forControlEvents:UIControlEventTouchUpInside];
		[buttonToAdd setTitle:@"DynamicButton" forState:UIControlStateNormal];
		buttonToAdd.frame = CGRectMake(80.0, 280.0, 160.0, 40.0);
		[self.view addSubview:buttonToAdd];
		//[buttonToAdd release];
		
		buttonCreated = YES;
	}
}

-(void)dynamicButtonAction {
	hiddenLabel.hidden = NO;
}
									

// The designated initializer.  Override if you create the controller programmatically and want to perform customization that is not appropriate for viewDidLoad.
/*
- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil {
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization.
    }
    return self;
}
*/


// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad {
    [super viewDidLoad];
	[self setTitle:@"View Two"];
	buttonCreated = NO;
}


/*
// Override to allow orientations other than the default portrait orientation.
- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation {
    // Return YES for supported orientations.
    return (interfaceOrientation == UIInterfaceOrientationPortrait);
}
*/

- (void)didReceiveMemoryWarning {
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc. that aren't in use.
}

- (void)viewDidUnload {
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}


- (void)dealloc {
    [super dealloc];
}


@end
