//
//  RootViewController.h
//  ThreeViewNav
//
//  Created by Brendan Christopher Fruin on 4/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface RootViewController : UIViewController {
	IBOutlet UILabel *theTextLabel;
}

@property(nonatomic, retain) IBOutlet UILabel *theTextLabel;

-(IBAction)changeBackgroundToBlackButtonPushed:(id)sender;
-(IBAction)changeTextButtonPushed:(id)sender;
-(IBAction)anotherViewButtonPushed:(id)sender;

@end
