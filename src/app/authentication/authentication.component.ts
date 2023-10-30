import { AuthorizationService } from './../services/authorization.service';
import { Component, inject } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { AuthentificationDataI } from '../intefaces/authorization.interface';

interface AuthentificationI {
    username: FormControl<string>;
    password: FormControl<string>;
}

@Component({
  selector: 'app-authentication',
  templateUrl: './authentication.component.html',
  styleUrls: ['./authentication.component.scss']
})
export class AuthenticationComponent {

    private _service = inject(AuthorizationService);

    form = new FormGroup<AuthentificationI>({
        username: new FormControl('', {nonNullable: true}),
        password: new FormControl('', {nonNullable: true})
    })

    data: AuthentificationDataI | undefined = undefined;

    submitForm(): void {
        const form = this.form.controls;

        this.data = {
            username: form.username.value,
            password: form.password.value
        };
        this._service.addUser(this.data);
    }
}
