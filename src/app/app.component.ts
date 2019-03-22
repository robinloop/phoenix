import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})
export class AppComponent {
  title = 'phoenix';
}

export const eel = window.eel;
eel.set_host('ws://localhost:8000');