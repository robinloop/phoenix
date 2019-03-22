import { Component, OnInit } from '@angular/core';
import { eel } from 'src/app/app.component';
import { Router } from '@angular/router';

@Component({
  selector: 'app-setup',
  templateUrl: './setup.component.html',
  styleUrls: ['./setup.component.less']
})
export class SetupComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
    eel.say_hello_py('Javascript World!')
  }
  
  completeSetup(){
    eel.get_header()(n => alert(n))
    this.router.navigateByUrl("main");
  }
}
