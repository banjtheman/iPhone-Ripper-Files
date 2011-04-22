//
//  SecondView.h
//  ThreeViewNav
//
//  Created by Brendan Christopher Fruin on 4/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>


@interface SecondView : UIViewController {
	BOOL buttonCreated;
	IBOutlet UILabel *hiddenLabel;
}

-(IBAction)anotherViewButtonPushed:(id)sender;
-(IBAction)anotherButtonPushed:(id)sender;

@end
