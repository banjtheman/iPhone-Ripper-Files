//
//  ThirdView.h
//  ThreeViewNav
//
//  Created by Brendan Christopher Fruin on 4/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>


@interface ThirdView : UIViewController {
	IBOutlet UILabel *hiddenLabel;
	IBOutlet UILabel *hiddenLabel2;
	IBOutlet UIButton *hiddenButton;
}

-(IBAction)oddLocationButtonPushed:(id)sender;
-(IBAction)hiddenButtonPressed:(id)sender;

@end
